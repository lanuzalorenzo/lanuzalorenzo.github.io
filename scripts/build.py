#!/usr/bin/env python3
"""Ensambla las páginas del sitio con el esqueleto del paquete de identidad.

    python3 scripts/build.py          # escribe los HTML en la raíz del repo
    python3 scripts/build.py --check  # falla si lo versionado no coincide

Solo biblioteca estándar. La cabecera, el pie y el documento salen de
`identidad/plantilla.tpl`; aquí solo se aportan los datos y el contenido de
`src/pages/`. Los HTML de la raíz son artefactos: se generan, no se editan a
mano, y el trabajo `verify` comprueba que están al día.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
SITE = "https://lanuzalorenzo.github.io"
VERSION_CSS = "20261126d"
VERSION_JS = "20261126a"
OG_IMAGE = f"{SITE}/assets/social/og-image.jpg?v=20261105b"
OG_IMAGE_ALT = "Lorenzo Lanuza — Senior Software Engineer &amp; Architect, .NET y Cloud Security"

sys.path.insert(0, str(ROOT / "identidad"))
from shell import Sitio  # noqa: E402

# Lo que no viaja en los campos de `pagina()`: favicons, sitemap y autoría.
HEAD_COMUN = """    <script>if (location.hash) document.documentElement.classList.add("landing-hash");</script>
    <meta property="og:updated_time" content="2026-11-05T00:00:00+01:00">
    <meta name="author" content="Lorenzo Lanuza Arellano">
    <link rel="icon" type="image/png" sizes="16x16" href="assets/marca/favicon-16.png?v=20261105a">
    <link rel="icon" href="favicon.svg?v=20261105a" type="image/svg+xml">
    <link rel="icon" href="favicon.png?v=20261105a" sizes="180x180" type="image/png">
    <link rel="apple-touch-icon" href="assets/marca/apple-touch-icon.png?v=20261105a" sizes="180x180">
    <link rel="sitemap" type="application/xml" title="Sitemap" href="/sitemap.xml">"""
SCRIPTS = f'    <script src="app.js?v={VERSION_JS}" defer></script>'

JSON_LD = """    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Lorenzo Lanuza Arellano",
      "url": "https://lanuzalorenzo.github.io/",
      "image": "https://lanuzalorenzo.github.io/assets/social/og-image.jpg?v=20261105b",
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
        "description": "Doce módulos de seguridad agrupados por capa del modelo Defense-in-Depth, con el estado y la evidencia de cada uno.",
        "og_title": "Portfolio de seguridad — Lorenzo Lanuza",
        "og_description": "Doce módulos de seguridad agrupados por capa del modelo Defense-in-Depth, con el estado real y la evidencia de cada uno.",
        "og_type": "website",
        "canonical": f"{SITE}/portfolio.html",
        "head_extra": "",
    },
    {
        "file": "comicteca.html",
        "title": "Comicteca — Lorenzo Lanuza",
        "description": "Comicteca, la aplicación principal del portfolio: una web Blazor WebAssembly y una API .NET 10 con los controles compartidos ya probados en el banco de pruebas.",
        "og_title": "Comicteca — Lorenzo Lanuza",
        "og_description": "Comicteca, la aplicación principal del portfolio: una web Blazor WebAssembly y una API .NET 10 con los controles compartidos ya probados en el banco de pruebas.",
        "og_type": "website",
        "canonical": f"{SITE}/comicteca.html",
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


def render_page(page: dict) -> str:
    content = (SRC / "pages" / page["file"]).read_text(encoding="utf-8").strip("\n")
    home = page["file"] == "index.html"
    sitio = Sitio(
        perfil="publica",
        estilos=["styles.css"],
        version=VERSION_CSS,
    )
    return sitio.pagina(
        titulo=page["title"],
        descripcion=page["description"],
        canonical=page["canonical"],
        og_titulo=page["og_title"],
        og_descripcion=page["og_description"],
        og_tipo=page["og_type"],
        imagen=OG_IMAGE,
        imagen_alt=OG_IMAGE_ALT,
        actual=page["file"],
        contenido=content,
        arriba="#inicio" if home else "#contenido",
        marca_svg="assets/marca/marca-tile.svg",
        menu_js="",
        head_extra=HEAD_COMUN + ("\n" + page["head_extra"].rstrip("\n") if page["head_extra"] else ""),
        scripts=SCRIPTS,
    )


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
        identidad = subprocess.run([sys.executable, str(ROOT / "identidad" / "verificar.py")])
        ejemplo = subprocess.run(
            [sys.executable, str(ROOT / "identidad" / "ejemplo" / "build.py"), "--check"]
        )
        if stale:
            print("HTML generado desactualizado: " + ", ".join(stale))
            print("Ejecuta `python3 scripts/build.py` y commitea el resultado.")
        if identidad.returncode != 0 or ejemplo.returncode != 0 or stale:
            return 1
        print(f"OK: {len(PAGES)} páginas generadas y al día")
        return 0

    print(f"OK: {len(PAGES)} páginas generadas")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
