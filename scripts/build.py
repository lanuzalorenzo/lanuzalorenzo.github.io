#!/usr/bin/env python3
"""Ensambla las páginas del sitio a partir de `src/partials` y `src/pages`.

    python3 scripts/build.py          # escribe los HTML en la raíz del repo
    python3 scripts/build.py --check  # falla si lo versionado no coincide

Solo biblioteca estándar. Los HTML de la raíz son artefactos: se generan, no se
editan a mano, y el trabajo `verify` comprueba que están al día.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
SITE = "https://lanuzalorenzo.github.io"

JSON_LD = """    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Lorenzo Lanuza Arellano",
      "url": "https://lanuzalorenzo.github.io/",
      "image": "https://lanuzalorenzo.github.io/assets/og-image.jpg?v=20261105a",
      "jobTitle": "Senior Software Engineer & Architect · .NET & Azure",
      "alumniOf": {
        "@type": "EducationalOrganization",
        "name": "IES Sierra de Guara"
      },
      "knowsAbout": [
        "Ingeniería de software",
        "Arquitectura de software",
        ".NET",
        "Microsoft Azure",
        "DevSecOps",
        "AppSec",
        "Cloud Security",
        "OAuth 2.0"
      ],
      "sameAs": [
        "https://www.linkedin.com/in/lanuzalorenzo",
        "https://github.com/lanuzalorenzo"
      ]
    }
    </script>
"""

# Secciones de la portada y página propia de cada detalle. La nav se genera
# desde aquí: una entrada nueva se añade en un solo sitio.
NAV = [
    ("perfil", "Perfil"),
    ("experiencia", "Experiencia"),
    ("proyectos", "Proyectos"),
]
NAV_GROUP = [
    ("portfolio.html", "Portfolio de seguridad"),
    ("api.html", "EcommerceApi"),
    ("ia.html", "IA aplicada"),
]

PAGES = [
    {
        "file": "index.html",
        "title": "Lorenzo Lanuza — Senior Software Engineer &amp; Architect · .NET &amp; Azure",
        "description": "Lorenzo Lanuza Arellano: ingeniero de software senior en .NET y Azure con seguridad aplicada. DevSecOps, AppSec y Cloud Security.",
        "og_title": "Lorenzo Lanuza — Senior Software Engineer &amp; Architect · .NET &amp; Azure",
        "og_description": "Ingeniero de software senior en .NET y Azure. Aplico la seguridad dentro del desarrollo: identidad, AppSec y pipeline con gates.",
        "og_type": "profile",
        "canonical": f"{SITE}/",
        "head_extra": JSON_LD,
    },
    {
        "file": "portfolio.html",
        "title": "Portfolio de seguridad — Lorenzo Lanuza",
        "description": "Doce módulos de seguridad agrupados por capa del modelo Defense-in-Depth sobre una sola carga de trabajo, con el estado y la evidencia de cada uno.",
        "og_title": "Portfolio de seguridad — Lorenzo Lanuza",
        "og_description": "Doce módulos de seguridad agrupados por capa del modelo Defense-in-Depth, con el estado real y la evidencia de cada uno.",
        "og_type": "website",
        "canonical": f"{SITE}/portfolio.html",
        "head_extra": "",
    },
    {
        "file": "api.html",
        "title": "EcommerceApi — Lorenzo Lanuza",
        "description": "El estado real de 28 controles y límites de EcommerceApi, la API .NET 10 que sirve de banco de pruebas al portfolio, con enlace a su evidencia.",
        "og_title": "EcommerceApi — Lorenzo Lanuza",
        "og_description": "El estado real de 28 controles y límites de la API .NET 10 que sirve de banco de pruebas al portfolio, con enlace a su evidencia.",
        "og_type": "website",
        "canonical": f"{SITE}/api.html",
        "head_extra": "",
    },
    {
        "file": "ia.html",
        "title": "IA aplicada — Lorenzo Lanuza",
        "description": "Guías, experimentos y un montaje en uso de IA aplicada al desarrollo: montar el entorno, trabajar con agentes, decidir qué sale de la red y medir lo que se afirma.",
        "og_title": "IA aplicada — Lorenzo Lanuza",
        "og_description": "Guías, experimentos y un montaje en uso de IA aplicada: montar el entorno, trabajar con agentes, decidir qué sale de la red y medir lo que se afirma.",
        "og_type": "website",
        "canonical": f"{SITE}/ia.html",
        "head_extra": "",
    },
]


def render_nav(page: str) -> str:
    """Devuelve la nav con enlaces relativos a la página que la contiene."""
    home = page == "index.html"
    lines = []

    for anchor, label in NAV:
        href = f"#{anchor}" if home else f"index.html#{anchor}"
        lines.append(f'        <a href="{href}">{label}</a>')

    lines.append('        <div class="site-nav-group" role="group" aria-label="Proyectos y laboratorios">')
    for target, label in NAV_GROUP:
        current = ' class="is-active" aria-current="page"' if target == page else ""
        lines.append(f'          <a href="{target}"{current}>{label}</a>')
    lines.append("        </div>")

    lines.append('        <div class="site-nav-group">')
    lines.append('          <a href="%s">Contacto</a>' % ("#contacto" if home else "index.html#contacto"))
    lines.append("        </div>")
    return "\n".join(lines)


def render_page(page: dict) -> str:
    shell = (SRC / "partials" / "shell.html").read_text(encoding="utf-8")
    content = (SRC / "pages" / page["file"]).read_text(encoding="utf-8").strip("\n")
    home = page["file"] == "index.html"

    fields = {
        "{{title}}": page["title"],
        "{{description}}": page["description"],
        "{{og_title}}": page["og_title"],
        "{{og_description}}": page["og_description"],
        "{{og_type}}": page["og_type"],
        "{{canonical}}": page["canonical"],
        "{{head_extra}}": page["head_extra"].rstrip("\n"),
        "{{nav}}": render_nav(page["file"]),
        "{{content}}": content,
        "{{home_href}}": "#inicio" if home else "index.html",
        "{{top_href}}": "#inicio" if home else "#contenido",
    }

    for token, value in fields.items():
        if token not in shell:
            raise SystemExit(f"build: falta el token {token} en src/partials/shell.html")
        shell = shell.replace(token, value)

    leftover = sorted(set(re.findall(r"\{\{[a-z_]+\}\}", shell)))
    if leftover:
        raise SystemExit(f"build: tokens sin resolver: {', '.join(leftover)}")
    return shell


def main(argv: list[str]) -> int:
    check = "--check" in argv
    if not check and argv:
        raise SystemExit("uso: python3 scripts/build.py [--check]")

    stale = []
    for page in PAGES:
        target = ROOT / page["file"]
        rendered = render_page(page)
        if check:
            current = target.read_text(encoding="utf-8") if target.exists() else ""
            if current != rendered:
                stale.append(page["file"])
        else:
            target.write_text(rendered, encoding="utf-8")

    if check:
        if stale:
            print("HTML generado desactualizado: " + ", ".join(stale))
            print("Ejecuta `python3 scripts/build.py` y commitea el resultado.")
            return 1
        print(f"OK: {len(PAGES)} páginas generadas y al día")
        return 0

    print(f"OK: {len(PAGES)} páginas generadas")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
