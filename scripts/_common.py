#!/usr/bin/env python3
"""Fonctions partagées par les scripts du système de contextes V2."""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

SYSTEM_ROOT = Path(__file__).resolve().parents[1]
CONTEXTS_ROOT = SYSTEM_ROOT / "contexts"
ARCHIVE_ROOT = SYSTEM_ROOT / "_ARCHIVE"
SKELETON_ROOT = SYSTEM_ROOT / "skeleton"
TEMPLATE_ROOT = SYSTEM_ROOT / "template"

NOTE_KINDS = {
    "atomic": ("ATO", "atomic", "note-atomic.md", "Notes atomiques", "Aucune note atomique."),
    "thematic": ("THM", "thematic", "note-thematic.md", "Notes thématiques", "Aucune note thématique."),
    "glossary": ("GLO", "glossary", "note-glossary.md", "Glossaire", "Aucune entrée de glossaire."),
    "decision-record": (
        "DRE",
        "decision-records",
        "note-decision-record.md",
        "Decision records",
        "Aucun decision record.",
    ),
}


def slugify(value: str, max_words: int = 12) -> str:
    """Transforme un titre en slug ASCII utilisable dans un nom de fichier."""
    text = unicodedata.normalize("NFKD", value)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.replace("'", " ").replace("’", " ")
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    words = [w for w in text.split("-") if w]
    return "-".join(words[:max_words]) or "sans-titre"


def resolve_context(value: str, *, must_exist: bool = True) -> Path:
    """Accepte un nom de contexte ou un chemin, et le garde dans le système."""
    raw = Path(value)
    candidates = [raw if raw.is_absolute() else SYSTEM_ROOT / raw, CONTEXTS_ROOT / value]
    for candidate in candidates:
        if candidate.exists() and candidate.is_dir():
            path = candidate.resolve()
            break
    else:
        if must_exist:
            raise SystemExit(f"Contexte introuvable : {value}")
        path = (CONTEXTS_ROOT / value).resolve()

    try:
        path.relative_to(SYSTEM_ROOT)
    except ValueError as exc:
        raise SystemExit("Le contexte doit être dans ce dossier.") from exc
    return path


def title_of(path: Path) -> str:
    """Le premier titre de niveau 1 du fichier, sinon son nom."""
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except (OSError, UnicodeDecodeError):
        pass
    return path.stem


def frontmatter_of(path: Path) -> dict[str, str]:
    """Frontmatter YAML à plat. Suffisant ici : aucune valeur imbriquée."""
    fields: dict[str, str] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return fields
    if not lines or lines[0].strip() != "---":
        return fields
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line and not line.startswith((" ", "-", "#")):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields


def next_id(folder: Path, prefix: str) -> str:
    """Calcule l'identifiant suivant en scannant les fichiers présents.

    Aucun compteur n'est tenu : un compteur peut mentir, le disque non.
    """
    highest = 0
    if folder.exists():
        for path in folder.glob(f"{prefix}*.md"):
            match = re.match(rf"^{prefix}(\d+)", path.stem)
            if match:
                highest = max(highest, int(match.group(1)))
    return f"{prefix}{highest + 1:05d}"


def iter_dirs(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith("."))


def content_files(folder: Path, pattern: str = "*") -> list[Path]:
    """Les fichiers d'un dossier, README exclu."""
    if not folder.exists():
        return []
    return sorted(
        p for p in folder.glob(pattern) if p.is_file() and p.name != "README.md" and not p.name.startswith(".")
    )
