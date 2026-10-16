#!/usr/bin/env python3
"""Ajoute une source documentaire, et journalise son ingestion.

Deux modes :
  source_add.py <contexte> <fichier|url> --titre "…" --intention recherche
  source_add.py <contexte> --mark-ingested SRC00001 --status complete --notes ATO00001,ATO00002

Ce qui sera analysé est le texte intégral, jamais un résumé. Une extraction ratée
produit un marqueur visible, jamais un fichier vide : un fichier vide laisse croire
qu'on a lu.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import re
import shutil
import urllib.request
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from _common import TEMPLATE_ROOT, content_files, next_id, resolve_context, slugify
from refresh_readmes import refresh_context, write_root_readmes

FAILED_MARKER = "⚠️ EXTRACTION ÉCHOUÉE"
MIN_WORDS = 50
READABLE = {".md", ".txt", ".markdown", ".rst"}


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extract_pdf(path: Path) -> str:
    try:
        import fitz  # PyMuPDF
    except ImportError as exc:
        raise SystemExit(
            "PyMuPDF manquant. Installer : .venv/bin/pip install -r requirements.txt"
        ) from exc
    with fitz.open(path) as document:
        return "\n\n".join(page.get_text("text") for page in document)


def extract_html(raw: str) -> tuple[str, str]:
    """Retourne (titre, texte). Extraction volontairement simple, sans dépendance."""
    title_match = re.search(r"<title[^>]*>(.*?)</title>", raw, re.S | re.I)
    title = html.unescape(title_match.group(1)).strip() if title_match else ""
    body = re.sub(r"(?is)<(script|style|nav|footer|header)[^>]*>.*?</\1>", " ", raw)
    body = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>", "\n", body)
    body = re.sub(r"<[^>]+>", " ", body)
    body = html.unescape(body)
    body = re.sub(r"[ \t]+", " ", body)
    body = re.sub(r"\n\s*\n\s*\n+", "\n\n", body)
    return title, body.strip()


def fill_frontmatter(text: str, values: dict[str, str]) -> str:
    lines = text.splitlines()
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    known = set()
    for i in range(1, end):
        key = lines[i].split(":", 1)[0].strip()
        known.add(key)
        if key in values:
            lines[i] = f"{key}: {values[key]}"
    for key, value in values.items():
        if key not in known:
            lines.insert(end, f"{key}: {value}")
            end += 1
    return "\n".join(lines)


# ----------------------------------------------------------------------- ingestion


def mark_ingested(context: Path, ident: str, status: str, notes: str, read_on: str = "") -> None:
    docs = context / "03-sources" / "documents"
    matches = [p for p in content_files(docs, "*.md") if p.stem.startswith(ident)]
    sessions = context / "03-sources" / "sessions"
    matches += [p for p in content_files(sessions, "*.md") if p.stem == ident]
    if not matches:
        raise SystemExit(f"Source introuvable : {ident}")
    source = matches[0]

    fingerprint_target = source
    if source.parent.name == "documents":
        raw = next((p for p in content_files(docs / "raw") if p.stem.startswith(ident)), None)
        fingerprint_target = raw or source

    log = context / "03-sources" / "ingestion-log.md"
    entry = "\n".join(
        [
            f"## {source.stem}",
            f"- chemin : {source.relative_to(context).as_posix()}",
            f"- état : {status}",
            f"- empreinte : sha256:{sha256_of(fingerprint_target)}",
            f"- lu le : {read_on or date.today().isoformat()}",
            f"- a produit : {notes or '—'}",
            "",
        ]
    )

    text = log.read_text(encoding="utf-8") if log.exists() else "# Journal d'ingestion\n\n"
    pattern = re.compile(rf"^## {re.escape(source.stem)}\n(?:.*\n)*?(?=^## |\Z)", re.M)
    text = pattern.sub("", text).rstrip() + "\n\n" + entry
    log.write_text(text, encoding="utf-8")
    print(f"journal mis à jour : {source.stem} — {status}")


# ---------------------------------------------------------------------------- ajout


def add_source(context: Path, target: str, title: str, intention: str, added: str = "") -> None:
    docs = context / "03-sources" / "documents"
    raw_dir, full_dir = docs / "raw", docs / "fulltext"
    for folder in (docs, raw_dir, full_dir):
        folder.mkdir(parents=True, exist_ok=True)

    ident = next_id(docs, "SRC")
    is_url = target.startswith(("http://", "https://"))
    url = target if is_url else ""
    extraction, fulltext_rel, kind = "ok", "", "text"

    if is_url:
        request = urllib.request.Request(target, headers={"User-Agent": "context-v2"})
        with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310
            payload = response.read()
        page = payload.decode("utf-8", errors="replace")
        found_title, body = extract_html(page)
        title = title or found_title or urlparse(target).netloc
        kind = "web"
        stem = f"{ident}-{slugify(title)}"
        (raw_dir / f"{stem}.html").write_text(page, encoding="utf-8")
        text = body
    else:
        origin = Path(target).expanduser()
        if not origin.is_file():
            raise SystemExit(f"Fichier introuvable : {target}")
        title = title or origin.stem
        suffix = origin.suffix.lower()
        stem = f"{ident}-{slugify(title)}"
        shutil.copy2(origin, raw_dir / f"{stem}{suffix}")
        if suffix == ".pdf":
            kind, text = "pdf", extract_pdf(origin)
        elif suffix in READABLE:
            kind, text = "text", ""  # déjà lisible : pas de fulltext séparé
        else:
            kind, text = suffix.lstrip("."), origin.read_text(encoding="utf-8", errors="replace")

    if text:
        if len(text.split()) < MIN_WORDS:
            extraction = "failed"
            text = (
                f"{FAILED_MARKER}\n\n"
                f"Moins de {MIN_WORDS} mots extraits de `{stem}`. PDF scanné sans couche texte, "
                "ou conversion à refaire. Cette source ne doit produire aucune note.\n"
            )
        (full_dir / f"{stem}.md").write_text(text, encoding="utf-8")
        fulltext_rel = f"fulltext/{stem}.md"

    raw_file = next(p for p in raw_dir.glob(f"{stem}.*"))
    fiche = fill_frontmatter(
        (TEMPLATE_ROOT / "source-document.md").read_text(encoding="utf-8"),
        {
            "added": added or date.today().isoformat(),
            "kind": kind,
            "intention": intention,
            "url": url,
            "raw": f"raw/{raw_file.name}",
            "fulltext": fulltext_rel,
            "extraction": extraction,
            "reliability": "medium",
        },
    )
    fiche = re.sub(r"^# .*$", f"# {title}", fiche, count=1, flags=re.M)
    (docs / f"{stem}.md").write_text(fiche, encoding="utf-8")

    refresh_context(context)
    write_root_readmes()

    words = len(text.split()) if text else "—"
    print(f"{ident} ajouté : {stem}")
    print(f"  brut      : {raw_file.relative_to(context)}")
    print(f"  texte     : {fulltext_rel or 'déjà lisible, pas de conversion'}")
    print(f"  extraction: {extraction} ({words} mots)")
    if extraction == "failed":
        print("  → NE PAS ingérer cette source tant que sa matière n'est pas figée.")
    print(f"  fiche     : à compléter — {(docs / f'{stem}.md').relative_to(context)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ajouter une source, ou marquer une ingestion.")
    parser.add_argument("contexte")
    parser.add_argument("target", nargs="?", help="Chemin d'un fichier ou URL")
    parser.add_argument("--titre", default="")
    parser.add_argument("--intention", default="recherche", help="recherche, entretien, veille…")
    parser.add_argument("--added", default="", help="Date d'entrée, si la source vient d'ailleurs")
    parser.add_argument("--mark-ingested", metavar="SRC00001")
    parser.add_argument("--status", default="complete", choices=["complete", "partial", "needs-review"])
    parser.add_argument("--notes", default="", help="Identifiants des notes produites")
    parser.add_argument("--lu-le", default="", help="Date de lecture, si l'ingestion vient d'ailleurs")
    args = parser.parse_args()

    context = resolve_context(args.contexte)
    if args.mark_ingested:
        mark_ingested(context, args.mark_ingested, args.status, args.notes, args.lu_le)
        refresh_context(context)
        return
    if not args.target:
        raise SystemExit("Donner un fichier/URL, ou utiliser --mark-ingested.")
    add_source(context, args.target, args.titre, args.intention, args.added)


if __name__ == "__main__":
    main()
