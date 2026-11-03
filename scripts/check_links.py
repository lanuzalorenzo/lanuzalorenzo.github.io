#!/usr/bin/env python3
"""Comprueba enlaces relativos en Markdown y HTML. No sale a Internet.

Valida rutas dentro del repositorio y, en HTML, que la ancla apuntada exista.
Ignora enlaces absolutos, correo y esquemas como `data:` o `javascript:`.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", "node_modules", "_site", "src"}
SUFFIXES = {".md", ".html", ".htm"}
HTML_SUFFIXES = {".html", ".htm"}
MD_LINK = re.compile(r"!?\[[^\]]*\]\((?:<([^>]+)>|([^)\s]+))")
HTML_ATTR = re.compile(r"""(?:href|src)\s*=\s*(?:"([^"]*)"|'([^']*)')""", re.IGNORECASE)
HTML_ID = re.compile(r"""\sid\s*=\s*(?:"([^"]*)"|'([^']*)')""", re.IGNORECASE)

_anchors: dict[Path, set[str]] = {}


def anchors(path: Path) -> set[str]:
    """Devuelve los `id` declarados en un documento HTML."""
    if path not in _anchors:
        text = path.read_text(encoding="utf-8", errors="replace")
        _anchors[path] = {double or single for double, single in HTML_ID.findall(text)}
    return _anchors[path]


def documents() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.suffix.lower() in SUFFIXES
        and not (SKIP & set(path.relative_to(ROOT).parts))
    ]


def targets(path: Path, text: str):
    if path.suffix.lower() == ".md":
        for angle, plain in MD_LINK.findall(text):
            yield angle or plain
    else:
        for double, single in HTML_ATTR.findall(text):
            yield double or single


def main() -> int:
    missing: list[tuple[Path, str]] = []
    for path in documents():
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in targets(path, text):
            target = html.unescape(raw).strip()
            if not target or target.startswith(("mailto:", "tel:", "data:", "javascript:")):
                continue
            parsed = urlparse(target)
            if parsed.scheme or parsed.netloc:
                continue
            clean = unquote(parsed.path)
            if clean:
                base = ROOT if clean.startswith("/") else path.parent
                resolved = (base / clean.lstrip("/")).resolve()
                if not resolved.exists():
                    missing.append((path.relative_to(ROOT), target))
                    continue
            else:
                resolved = path
            fragment = unquote(parsed.fragment)
            if fragment and resolved.suffix.lower() in HTML_SUFFIXES:
                if fragment not in anchors(resolved):
                    missing.append((path.relative_to(ROOT), target))

    if missing:
        for path, target in missing:
            print(f"{path}: {target}")
        print(f"\n{len(missing)} enlaces relativos rotos")
        return 1

    print(f"OK: {len(documents())} documentos sin enlaces relativos rotos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
