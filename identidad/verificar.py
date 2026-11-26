#!/usr/bin/env python3
"""Comprueba que el paquete de identidad está al día y es consumible.

    python3 identidad/verificar.py           # comprueba
    python3 identidad/verificar.py --update  # reescribe SHA256SUMS

Comprueba cuatro cosas: que `identidad.css` coincide con lo que extrae
`extraer.py` de `styles.css`, que la marca del paquete es la que sirve la web,
que la versión de la cabecera es la de `VERSION` y que las huellas corresponden.
En `--update`, si el contenido cambia y `VERSION` no ha cambiado respecto a
`HEAD`, falla: una versión no puede publicar contenido distinto dos veces.

Solo biblioteca estándar.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PAQUETE = RAIZ / "identidad"
FUENTE_MARCA = RAIZ / "assets" / "marca" / "marca-tile.svg"

# Lo que consume una web: si cambia un byte, sube la versión.
MANIFIESTO = ("identidad.css", "plantilla.tpl", "shell.py", "menu.js", "marca-tile.svg", "VERSION")


def huella(ruta: Path) -> str:
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def sumas() -> str:
    return "".join(f"{huella(PAQUETE / nombre)}  {nombre}\n" for nombre in MANIFIESTO)


def en_git(ruta: str) -> str | None:
    """Contenido versionado de `ruta`, o None si git no está o el archivo no existe."""
    try:
        resultado = subprocess.run(
            ["git", "show", f"HEAD:{ruta}"],
            cwd=RAIZ, capture_output=True, text=True, check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return resultado.stdout if resultado.returncode == 0 else None


def main(argv: list[str]) -> int:
    actualizar = "--update" in argv
    if not actualizar and argv:
        raise SystemExit("uso: python3 identidad/verificar.py [--update]")
    fallos: list[str] = []

    sys.path.insert(0, str(PAQUETE))
    import extraer  # noqa: E402  (mismo directorio)

    version = (PAQUETE / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fallos.append(f"VERSION no es semver: {version!r}")

    css = (PAQUETE / "identidad.css").read_text(encoding="utf-8")
    if f"Versión {version}." not in css:
        fallos.append("identidad.css no declara la versión de VERSION")
    if css != extraer.generar():
        fallos.append(
            "identidad.css no coincide con styles.css: "
            "ejecuta `python3 identidad/extraer.py`"
        )

    marca = PAQUETE / "marca-tile.svg"
    if marca.read_bytes() != FUENTE_MARCA.read_bytes():
        fallos.append(
            "marca-tile.svg no es el de assets/marca: "
            "cópialo con `cp assets/marca/marca-tile.svg identidad/`"
        )

    calculadas = sumas()
    fichero = PAQUETE / "SHA256SUMS"
    versionadas = fichero.read_text(encoding="utf-8") if fichero.exists() else ""
    version_en_git = en_git("identidad/VERSION")

    if actualizar and calculadas != versionadas:
        if version_en_git is not None and version == version_en_git.strip():
            fallos.append(
                "el contenido cambió pero VERSION sigue en "
                f"{version}: súbela en identidad/VERSION y regenera"
            )

    if fallos:
        for fallo in fallos:
            print(f"FALLO: {fallo}")
        return 1

    if actualizar:
        fichero.write_text(calculadas, encoding="utf-8")
        print(f"OK: SHA256SUMS actualizado para la versión {version}")
        return 0
    if calculadas != versionadas:
        print("FALLO: SHA256SUMS no corresponde: ejecuta `--update`")
        return 1
    print(f"OK: identidad {version} al día ({len(MANIFIESTO)} archivos)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
