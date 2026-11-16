"""Shell de la identidad para una web nueva.

    from shell import Sitio

    sitio = Sitio(perfil="publica", estilos=["styles.css"], repo="https://…")
    html = sitio.pagina(
        titulo="…",
        descripcion="…",
        canonical="https://…/",
        nav=[("index.html#perfil", "Perfil"), {"grupo": "Proyectos"}, ("api.html", "API")],
        actual="api.html",
        contenido=cuerpo,
    )

Solo biblioteca estándar. El perfil decide qué se emite: `publica` lleva datos
para compartir y enlace al código; `local` no los lleva y se declara `noindex`.
"""

from __future__ import annotations

import re
from pathlib import Path

PLANTILLA = Path(__file__).resolve().with_name("plantilla.tpl")

# Un bloque condicional: `<!-- perfil:local -->…<!-- /perfil:local -->` o
# `<!-- si:repo -->…<!-- /si:repo -->`.
BLOQUE = re.compile(
    r"^[ \t]*<!-- (perfil|si):([a-z_]+) -->\n?(.*?)^[ \t]*<!-- /(?:perfil|si):\2 -->[ \t]*\n?",
    re.S | re.M,
)

TOKEN = re.compile(r"\{\{([a-z_]+)\}\}")

PERFILES = ("publica", "local")


class Sitio:
    """Compone páginas con la cabecera, el pie y los tokens de la marca."""

    def __init__(
        self,
        perfil: str = "publica",
        raiz: str = "",
        estilos: tuple[str, ...] | list[str] = (),
        version: str = "",
        repo: str = "",
        nota: str = "",
        plantilla: Path | str | None = None,
    ) -> None:
        if perfil not in PERFILES:
            raise ValueError(f"perfil desconocido: {perfil!r}; usa {' o '.join(PERFILES)}")
        self.perfil = perfil
        # La raíz se normaliza a una sola forma: vacía o terminada en barra.
        self.raiz = raiz if raiz in ("", "/") or raiz.endswith("/") else f"{raiz}/"
        self.estilos = list(estilos)
        self.version = version
        self.repo = repo
        self.nota = nota
        self.plantilla = Path(plantilla) if plantilla else PLANTILLA

    # ── Piezas ────────────────────────────────────────────────────────
    def absoluta(self, href: str) -> str:
        """Aplica la raíz a una ruta relativa; deja intactas las absolutas y los anclas."""
        if href.startswith(("#", "/", "http://", "https://", "mailto:")):
            return href
        return f"{self.raiz}{href}"

    def estilos_html(self) -> str:
        lineas = []
        for href in self.estilos:
            destino = self.absoluta(href)
            consulta = f"?v={self.version}" if self.version and "?" not in destino else ""
            lineas.append(f'    <link rel="stylesheet" href="{destino}{consulta}">')
        return "\n".join(lineas)

    def nav_html(self, items, actual: str | None = None) -> str:
        lineas: list[str] = []
        grupo = False
        for item in items:
            if isinstance(item, dict) and "grupo" in item:
                if grupo:
                    lineas.append("        </div>")
                etiqueta = item["grupo"]
                lineas.append(
                    f'        <div class="site-nav-group" role="group" aria-label="{etiqueta}">'
                )
                grupo = True
                continue
            href, etiqueta = item
            if actual and actual != "index.html" and href.startswith("#"):
                href = f"index.html{href}"
            href = self.absoluta(href)
            activo = ' class="is-active" aria-current="page"' if href == actual else ""
            sangria = "          " if grupo else "        "
            lineas.append(f'{sangria}<a href="{href}"{activo}>{etiqueta}</a>')
        if grupo:
            lineas.append("        </div>")
        return "\n".join(lineas)

    def og_meta(self, titulo: str, descripcion: str, canonical: str, tipo: str,
                imagen: str = "", imagen_alt: str = "") -> str:
        lineas = [
            f'    <meta property="og:type" content="{tipo}">',
            '    <meta property="og:locale" content="es_ES">',
            f'    <meta property="og:title" content="{titulo}">',
            f'    <meta property="og:description" content="{descripcion}">',
        ]
        if canonical:
            lineas.append(f'    <meta property="og:url" content="{canonical}">')
        if imagen:
            lineas.append(f'    <meta property="og:image" content="{imagen}">')
            lineas.append('    <meta property="og:image:width" content="1200">')
            lineas.append('    <meta property="og:image:height" content="630">')
            if imagen_alt:
                lineas.append(f'    <meta property="og:image:alt" content="{imagen_alt}">')
        lineas += [
            '    <meta name="twitter:card" content="summary_large_image">',
            f'    <meta name="twitter:title" content="{titulo}">',
            f'    <meta name="twitter:description" content="{descripcion}">',
        ]
        if canonical:
            lineas.append(f'    <meta name="twitter:url" content="{canonical}">')
        if imagen:
            lineas.append(f'    <meta name="twitter:image" content="{imagen}">')
        return "\n".join(lineas)

    # ── Página ────────────────────────────────────────────────────────
    def pagina(self, **campos) -> str:
        if "titulo" not in campos or "contenido" not in campos:
            raise TypeError("pagina() necesita al menos `titulo` y `contenido`")

        titulo = campos.pop("titulo")
        contenido = campos.pop("contenido")
        descripcion = campos.pop("descripcion", "")
        canonical = campos.pop("canonical", "")
        nav = campos.pop("nav", ())
        actual = campos.pop("actual", None)
        imagen = campos.pop("imagen", "")
        imagen_alt = campos.pop("imagen_alt", "")
        tipo = campos.pop("og_tipo", "website")
        if "inicio" in campos:
            inicio = campos.pop("inicio")
        elif actual in (None, "index.html"):
            inicio = "#inicio"
        else:
            inicio = f"{self.raiz}index.html"
        arriba = campos.pop("arriba", "#contenido")

        relleno = {
            "titulo": titulo,
            "descripcion": descripcion,
            "canonical": canonical,
            "og_meta": self.og_meta(
                campos.pop("og_titulo", titulo),
                campos.pop("og_descripcion", descripcion),
                canonical, tipo, imagen, imagen_alt,
            ),
            "estilos": self.estilos_html(),
            "nav": self.nav_html(nav, actual),
            "contenido": contenido,
            "inicio": inicio,
            "arriba": arriba,
            "marca_svg": f"{self.raiz}_identidad/marca-tile.svg",
            "menu_js": f"{self.raiz}_identidad/menu.js" + (f"?v={self.version}" if self.version else ""),
            "repo": self.repo if self.perfil == "publica" else "",
            "pie_nota": self.nota,
        }
        relleno.update(campos)

        plantilla = self.plantilla.read_text(encoding="utf-8")
        html = self._bloques(plantilla, relleno)
        for nombre, valor in relleno.items():
            html = html.replace("{{" + nombre + "}}", str(valor))

        faltan = sorted(set(TOKEN.findall(html)))
        if faltan:
            raise SystemExit(
                "shell: campos sin resolver: " + ", ".join(faltan)
            )
        return html

    def _bloques(self, plantilla: str, campos: dict) -> str:
        def resolver(match: re.Match) -> str:
            clase, nombre, cuerpo = match.group(1), match.group(2), match.group(3)
            if clase == "perfil":
                return cuerpo if nombre == self.perfil else ""
            return cuerpo if campos.get(nombre) else ""

        while True:
            nuevo = BLOQUE.sub(resolver, plantilla)
            if nuevo == plantilla:
                return nuevo
            plantilla = nuevo
