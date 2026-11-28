"""Shell de la identidad para una web nueva.

    from shell import Sitio

    sitio = Sitio(perfil="publica", estilos=["styles.css"])
    html = sitio.pagina(
        titulo="…",
        descripcion="…",
        canonical="https://…/",
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

# La nav es de la marca, no de cada web: los mismos destinos y el mismo orden
# en todas. `actual` marca la sección en la que está el visitante.
NAV = (
    ("https://lanuzalorenzo.github.io/portfolio.html", "Portfolio de seguridad", "portfolio.html"),
    ("https://lanuzalorenzo.github.io/comicteca.html", "Comicteca", "comicteca.html"),
    ("https://lanuzalorenzo.github.io/api.html", "EcommerceApi", "api.html"),
    ("https://lanuzalorenzo.github.io/eventos.html", "eventos-api", "eventos.html"),
    ("https://lanuzalorenzo.github.io/ia.html", "IA aplicada", "ia.html"),
    ("https://lanuzalorenzo.github.io/biblioteca-tecnica/", "Biblioteca", "biblioteca"),
    ("https://lanuzalorenzo.github.io/#contacto", "Contacto", "contacto"),
)
CONTACTO = "Contacto"


class Sitio:
    """Compone páginas con la cabecera, el pie y los tokens de la marca."""

    def __init__(
        self,
        perfil: str = "publica",
        raiz: str = "",
        estilos: tuple[str, ...] | list[str] = (),
        version: str = "",
        nota: str = "© 2026 Lorenzo Lanuza",
        plantilla: Path | str | None = None,
    ) -> None:
        if perfil not in PERFILES:
            raise ValueError(f"perfil desconocido: {perfil!r}; usa {' o '.join(PERFILES)}")
        self.perfil = perfil
        # La raíz se normaliza a una sola forma: vacía o terminada en barra.
        self.raiz = raiz if raiz in ("", "/") or raiz.endswith("/") else f"{raiz}/"
        self.estilos = list(estilos)
        self.version = version
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

    def nav_canonica(self, actual: str | None = None) -> str:
        """La nav de la marca, idéntica en todas las webs que consumen el paquete."""
        def enlace(item) -> str:
            href, etiqueta, slug = item
            activo = ' class="is-active" aria-current="page"' if actual == slug else ""
            return f'          <a href="{href}"{activo}>{etiqueta}</a>'

        grupo = "\n".join(enlace(item) for item in NAV if item[1] != CONTACTO)
        contacto = "\n".join(enlace(item) for item in NAV if item[1] == CONTACTO)
        return (
            '        <div class="site-nav-group" role="group" aria-label="Proyectos, laboratorios y biblioteca">\n'
            f"{grupo}\n"
            "        </div>\n"
            '        <div class="site-nav-group">\n'
            f"{contacto}\n"
            "        </div>"
        )

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
                href = f"{self.raiz or '/'}{href}"
            href = self.absoluta(href)
            activo = ' class="is-active" aria-current="page"' if actual and href in (actual, self.absoluta(actual)) else ""
            sangria = "          " if grupo else "        "
            lineas.append(f'{sangria}<a href="{href}"{activo}>{etiqueta}</a>')
        if grupo:
            lineas.append("        </div>")
        return "\n".join(lineas)

    # ── Fragmentos para un consumidor con layout propio ────────────────
    def _fragmento(self, etiqueta: str, campos: dict) -> str:
        """Devuelve un bloque de la plantilla con sus condicionales y tokens."""
        plantilla = self.plantilla.read_text(encoding="utf-8")
        patron = rf'<{etiqueta} class="site-{etiqueta}">.*?</{etiqueta}>'
        encontrado = re.search(patron, plantilla, re.S)
        if not encontrado:
            raise SystemExit(f"shell: falta <{etiqueta}> en {self.plantilla.name}")
        bloque = self._bloques(encontrado.group(0), campos)
        for nombre, valor in campos.items():
            bloque = bloque.replace("{{" + nombre + "}}", str(valor))
        faltan = sorted(set(TOKEN.findall(bloque)))
        if faltan:
            raise SystemExit(
                "shell: campos sin resolver en el fragmento: " + ", ".join(faltan)
            )
        return bloque

    def cabecera(self, nav: str = "", inicio: str | None = None) -> str:
        """Cabecera de la plantilla; `nav` llega ya compuesta por el consumidor."""
        return self._fragmento("header", {
            "nav": nav,
            "inicio": inicio or "/",
            "marca_svg": f"{self.raiz}_identidad/marca-tile.svg",
        })

    def pie(self, inicio: str | None = None, arriba: str = "#contenido", nota: str = "") -> str:
        """Pie de la plantilla, con el enlace al código del perfil público."""
        return self._fragmento("footer", {
            "inicio": inicio or "/",
            "arriba": arriba,
            "pie_nota": nota,
            "marca_svg": f"{self.raiz}_identidad/marca-tile.svg",
        })

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
            if imagen_alt:
                lineas.append(f'    <meta name="twitter:image:alt" content="{imagen_alt}">')
        return "\n".join(lineas)

    # ── Página ────────────────────────────────────────────────────────
    def pagina(self, **campos) -> str:
        if "titulo" not in campos or not ("contenido" in campos or "cuerpo" in campos):
            raise TypeError("pagina() necesita `titulo` y `contenido` o `cuerpo`")

        titulo = campos.pop("titulo")
        contenido = campos.pop("contenido", None)
        cuerpo = campos.pop("cuerpo", None)
        if contenido is not None and cuerpo is not None:
            raise TypeError("pagina() acepta `contenido` o `cuerpo`, no los dos")
        if cuerpo is None:
            if contenido is None:
                raise TypeError("pagina() necesita `contenido` o `cuerpo`")
            cuerpo = f'    <main id="contenido">\n{contenido}\n    </main>'
        descripcion = campos.pop("descripcion", "")
        canonical = campos.pop("canonical", "")
        nav = campos.pop("nav", None)
        actual = campos.pop("actual", None)
        imagen = campos.pop("imagen", "")
        imagen_alt = campos.pop("imagen_alt", "")
        tipo = campos.pop("og_tipo", "website")
        # La marca enlaza a la raíz del dominio, también desde una web servida
        # en un subdirectorio. Quien no viva en la raíz pasa `inicio` explícito.
        inicio = campos.pop("inicio", "/")
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
            "nav": (
                nav
                if isinstance(nav, str)
                else self.nav_html(nav, actual)
                if nav
                else self.nav_canonica(actual)
            ),
            "cuerpo": cuerpo,
            "inicio": inicio,
            "arriba": arriba,
            "marca_svg": campos.pop("marca_svg", f"{self.raiz}_identidad/marca-tile.svg"),
            "head_extra": campos.pop("head_extra", ""),
            "scripts": campos.pop("scripts", ""),
            "atributos_cuerpo": campos.pop("atributos_cuerpo", ""),
            "antes_cabecera": campos.pop("antes_cabecera", ""),
            "menu_js": f"{self.raiz}_identidad/menu.js" + (f"?v={self.version}" if self.version else ""),
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
