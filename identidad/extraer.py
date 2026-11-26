#!/usr/bin/env python3
"""Extrae la capa de marca de `styles.css` y escribe `identidad.css`.

    python3 identidad/extraer.py           # reescribe identidad.css
    python3 identidad/extraer.py --check   # falla si el versionado no coincide

La fuente es `styles.css` de esta web. Aquí no se decide nada: se copian las
reglas de los selectores que son marca y se descarta el resto. Si una regla
nueva de marca no aparece en la salida, se añade su selector a `MARCA`; no se
edita `identidad.css` a mano.

Solo biblioteca estándar.
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "styles.css"
DESTINO = RAIZ / "identidad" / "identidad.css"

# Selectores que forman la capa de marca. La comparación es exacta: el selector
# se escribe igual que en styles.css, sin comas.
MARCA = {
    # Base y tokens
    ":root",
    "*",
    "*::before",
    "*::after",
    "html",
    "body",
    "a",
    "button",
    "input",
    "::selection",
    ".sr-only",
    ".skip-link",
    ".skip-link:focus",
    ":focus-visible",
    'main > section[tabindex="-1"]:focus',
    ".eyebrow",
    # Estructura
    ".section-wrap",
    # Cabecera y navegación
    ".site-header",
    ".wordmark",
    ".wordmark img",
    ".site-nav",
    ".site-nav a",
    ".site-nav a.is-active",
    ".site-nav a.is-active::after",
    ".site-nav a:hover",
    ".site-nav.is-open",
    ".site-nav-group",
    ".site-nav-group::before",
    ".site-nav-group:first-child",
    ".site-nav-group:first-child::before",
    ".menu-toggle",
    ".menu-toggle span:not(.sr-only)",
    '.menu-toggle[aria-expanded="true"] .menu-line-top',
    '.menu-toggle[aria-expanded="true"] .menu-line-bottom',
    "html.menu-open",
    # Botones
    ".button",
    ".button:hover",
    ".button-dark",
    ".button-dark:hover",
    ".button-quiet",
    ".button-quiet:hover",
    ".button span",
    ".button-light",
    ".button-light:hover",
    # Pie
    ".site-footer",
    ".site-footer > a:not(.wordmark)",
    ".site-footer > span",
    ".site-footer a:hover",
    # Insignias de estado
    ".module-status",
    ".status-validated",
    ".status-partial",
    ".status-design",
    ".status-pending",
}

# At-rules: se recorren todos y se conserva el bloque solo si queda alguna regla
# de marca dentro. Así una regla nueva en `@media (min-width: …)` o en `@supports`
# no se pierde por no estar en una lista.


def dividir_selectores(texto: str) -> list[str]:
    """Parte una lista de selectores por las comas de primer nivel."""
    partes: list[str] = []
    actual = ""
    profundidad = 0
    for caracter in texto:
        if caracter == "(":
            profundidad += 1
        elif caracter == ")":
            profundidad -= 1
        if caracter == "," and profundidad == 0:
            partes.append(actual.strip())
            actual = ""
            continue
        actual += caracter
    partes.append(actual.strip())
    return [parte for parte in partes if parte]


def leer_hasta(css: str, i: int) -> tuple[str, int]:
    """Devuelve el texto hasta el siguiente `{` o `;` y la posición de ese signo."""
    inicio = i
    while i < len(css) and css[i] not in "{;":
        i += 1
    return css[inicio:i].strip(), i


def saltar_bloque(css: str, i: int) -> int:
    """Devuelve la posición tras el `}` que cierra el bloque abierto en `i`."""
    profundidad = 0
    while i < len(css):
        if css[i] == "{":
            profundidad += 1
        elif css[i] == "}":
            profundidad -= 1
            if profundidad == 0:
                return i + 1
        i += 1
    raise SystemExit("extraer: bloque sin cerrar en styles.css")


def analizar(css: str) -> list[tuple[str, str, str]]:
    """Devuelve nodos (tipo, preludio, cuerpo). `at` conserva sus hijos en bruto."""
    nodos: list[tuple[str, str, str]] = []
    i = 0
    while i < len(css):
        while i < len(css) and css[i].isspace():
            i += 1
        if i >= len(css):
            break
        if css.startswith("/*", i):
            fin = css.find("*/", i + 2)
            i = len(css) if fin < 0 else fin + 2
            continue
        preludio, i = leer_hasta(css, i)
        if i >= len(css):
            break
        if css[i] == ";":
            i += 1
            continue
        fin = saltar_bloque(css, i)
        cuerpo = css[i + 1 : fin - 1]
        if preludio.startswith("@"):
            nodos.append(("at", preludio, cuerpo))
        else:
            nodos.append(("regla", preludio, cuerpo))
        i = fin
    return nodos


def formatear_cuerpo(cuerpo: str, sangria: str) -> str:
    """Un declaración por línea, sin reordenar ni reinterpretar valores."""
    lineas = []
    for declaracion in cuerpo.split(";"):
        limpia = " ".join(declaracion.split())
        if limpia:
            lineas.append(f"{sangria}  {limpia};")
    return "\n".join(lineas)


def filtrar(nodos: list[tuple[str, str, str]]) -> list[str]:
    """Devuelve las reglas de marca ya formateadas, en su orden original."""
    salida: list[str] = []
    for tipo, preludio, cuerpo in nodos:
        if tipo == "regla":
            selectores = [s for s in dividir_selectores(preludio) if s in MARCA]
            if not selectores:
                continue
            salida.append(f"{', '.join(selectores)} {{\n{formatear_cuerpo(cuerpo, '')}\n}}")
            continue
        if tipo != "at":
            continue
        hijos = filtrar(analizar(cuerpo))
        if not hijos:
            continue
        interior = "\n".join("  " + linea for hijo in hijos for linea in hijo.splitlines())
        salida.append(f"{preludio} {{\n{interior}\n}}")
    return salida


def generar() -> str:
    css = FUENTE.read_text(encoding="utf-8")
    reglas = filtrar(analizar(css))
    version = (RAIZ / "identidad" / "VERSION").read_text(encoding="utf-8").strip()
    cabecera = (
        "/* Capa de marca · lanuzalorenzo.github.io\n"
        f"   Versión {version}. Archivo generado por identidad/extraer.py desde styles.css.\n"
        "   No editar a mano: cambia styles.css, sube VERSION y regenera. */\n"
    )
    return cabecera + "\n" + "\n\n".join(reglas) + "\n"


def main(argv: list[str]) -> int:
    check = "--check" in argv
    if not check and argv:
        raise SystemExit("uso: python3 identidad/extraer.py [--check]")
    generado = generar()
    if check:
        actual = DESTINO.read_text(encoding="utf-8") if DESTINO.exists() else ""
        if actual != generado:
            print("identidad.css desactualizado respecto a styles.css.")
            print("Ejecuta `python3 identidad/extraer.py` y commitea el resultado.")
            return 1
        print("OK: identidad.css al día")
        return 0
    DESTINO.write_text(generado, encoding="utf-8")
    print(f"OK: {DESTINO.relative_to(RAIZ)} escrito")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
