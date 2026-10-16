#!/usr/bin/env python3
"""Audite un contexte et écrit son verdict dans 01-state/health.md.

Entièrement mécanique : aucune de ces vérifications ne demande de jugement. C'est
pour ça qu'elle peut être garantie — une vérification écrite en prose et déclenchée
par personne ne se fait pas.
"""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path

from _common import NOTE_KINDS, content_files, frontmatter_of, iter_dirs, resolve_context, CONTEXTS_ROOT

LINK = re.compile(r"\[[^\]]*\]\(([^)#:]+?)\)")
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")


def notes_of(context: Path) -> list[tuple[str, Path]]:
    found = []
    for kind, (_prefix, folder, *_rest) in NOTE_KINDS.items():
        for path in content_files(context / "04-notes" / folder, "*.md"):
            found.append((kind, path))
    return found


def audit(context: Path) -> dict[str, list[str]]:
    findings: dict[str, list[str]] = {"bloquant": [], "à corriger": [], "à surveiller": []}

    # 1. Liens relatifs cassés
    for path in context.rglob("*.md"):
        for match in LINK.finditer(path.read_text(encoding="utf-8", errors="replace")):
            target = match.group(1).strip()
            if target.startswith(("http", "mailto")):
                continue
            if not (path.parent / target).exists():
                findings["à corriger"].append(f"lien cassé — {path.relative_to(context)} → {target}")

    # 2. Notes sans source : une note sans origine est une opinion, pas une connaissance
    ids = {frontmatter_of(p).get("id", p.stem.split("-")[0]) for _k, p in notes_of(context)}
    for kind, path in notes_of(context):
        fm = frontmatter_of(path)
        if fm.get("sources", "[]").strip() in ("", "[]"):
            findings["bloquant"].append(f"note sans source — {path.relative_to(context)}")
        if fm.get("status") == "superseded" and not fm.get("superseded_by"):
            findings["bloquant"].append(f"remplacée sans successeur — {path.relative_to(context)}")

    # 3. Rétroliens manquants : le lien remontant est le seul dont l'absence induit en erreur
    outgoing: dict[str, set[str]] = {}
    for _kind, path in notes_of(context):
        ident = frontmatter_of(path).get("id", path.stem.split("-")[0])
        outgoing[ident] = {m.group(1).split("-")[0] for m in WIKILINK.finditer(path.read_text(encoding="utf-8"))}
    for source_id, targets in outgoing.items():
        for target_id in targets:
            if target_id in ids and source_id not in outgoing.get(target_id, set()):
                findings["à corriger"].append(f"rétrolien manquant — {target_id} ne pointe pas vers {source_id}")

    # 4. Sources jamais ingérées, et extractions ratées
    log_text = ""
    log = context / "03-sources" / "ingestion-log.md"
    if log.exists():
        log_text = log.read_text(encoding="utf-8")
    docs = context / "03-sources" / "documents"
    for path in content_files(docs, "*.md"):
        if frontmatter_of(path).get("extraction") == "failed":
            findings["à surveiller"].append(f"extraction échouée — {path.stem} (ne pas ingérer)")
        elif path.stem not in log_text:
            findings["à surveiller"].append(f"source jamais ingérée — {path.stem}")
    for path in content_files(context / "03-sources" / "sessions", "SESSION-*.md"):
        if path.stem not in log_text:
            findings["à surveiller"].append(f"session jamais ingérée — {path.stem}")

    # 5. Fichiers d'état restés vides — un contexte qui ne dit pas où il en est
    for path in content_files(context / "01-state", "*.md"):
        if path.name == "health.md":
            continue
        text = re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S)
        body = "\n".join(l for l in text.splitlines() if not l.strip().startswith(("#", "|"))).strip()
        if not body:
            findings["à surveiller"].append(f"fichier vide — 01-state/{path.name}")

    # 6. Un README écrit à la main ne peut pas dire la vérité longtemps
    for path in context.rglob("README.md"):
        if "refresh_readmes.py" not in path.read_text(encoding="utf-8", errors="replace"):
            findings["à corriger"].append(f"README non généré — {path.relative_to(context)}")

    return findings


def report(context: Path) -> str:
    findings = audit(context)
    total = sum(len(v) for v in findings.values())
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    verdict = "sain" if total == 0 else ("défauts bloquants" if findings["bloquant"] else "défauts mineurs")

    lines = [
        "# Santé du contexte",
        "",
        f"Dernier `check` : {stamp} — **{verdict}** ({total} constat(s))",
        "",
    ]
    for level in ("bloquant", "à corriger", "à surveiller"):
        items = sorted(set(findings[level]))
        if items:
            lines += [f"## {level.capitalize()} ({len(items)})", "", *[f"- {i}" for i in items], ""]
    if total == 0:
        lines += ["Aucun défaut. Liens, sources, rétroliens et README sont cohérents.", ""]
    lines.append("<!-- Écrit par scripts/check.py — ne pas écrire à la main. -->")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Auditer un contexte V2.")
    parser.add_argument("contexte", nargs="?", help="Nom d'un contexte ; sinon tous.")
    args = parser.parse_args()

    targets = [resolve_context(args.contexte)] if args.contexte else iter_dirs(CONTEXTS_ROOT)
    if not targets:
        print("aucun contexte à auditer")
        return
    for context in targets:
        text = report(context)
        (context / "01-state" / "health.md").write_text(text, encoding="utf-8")
        print(f"--- {context.name} ---")
        print(text.split("<!--")[0].strip())


if __name__ == "__main__":
    main()
