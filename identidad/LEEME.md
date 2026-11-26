# Capa de identidad — consumo

Cabecera, pie, navegación, botones, insignias, tokens y el marco de página, en
un paquete que otra web consume tal cual. Se separa en dos piezas: el CSS con
los valores y la plantilla con el marcado. Cada web pone su contenido y su
distribución; no rehace la cabecera.

## Qué hay

| Archivo | Qué es |
|---|---|
| `identidad.css` | Tokens (incluido `--frame`), tipografía base, cabecera y nav, pie, botones, insignias, foco y movimiento reducido |
| `plantilla.tpl` | Shell completo con marcadores `{{...}}` y bloques por perfil |
| `shell.py` | Compone una página con la plantilla: perfiles, nav, metadatos, cuerpo y comprobación de marcadores |
| `menu.js` | Abrir y cerrar el menú en móvil; sin dependencias |
| `marca-tile.svg` | La baldosa de la marca, la misma que sirve la web |
| `SHA256SUMS` | Huellas de `identidad.css`, `plantilla.tpl`, `shell.py`, `menu.js`, `marca-tile.svg` y `VERSION` |
| `VERSION` | Versión del paquete; `identidad.css` la declara en su cabecera |

`extraer.py`, `verificar.py` y `ejemplo/` viven en el repositorio dueño y no se
distribuyen: son su mantenimiento, no el contrato de consumo.

## Perfiles

El perfil decide qué se emite. No es un tema: es qué metadatos y qué enlaces
tienen sentido en ese sitio.

| | `publica` | `local` |
|---|---|---|
| Open Graph y Twitter | Sí | No |
| `canonical` | Sí | No |
| `robots` | Sin directiva | `noindex, nofollow` |
| Enlace al código | Sí, si se pasa `repo` | No |

Una web publicada usa `publica`. Un visor que solo escucha en `127.0.0.1` usa
`local`: no tiene sentido anunciar en redes una URL que nadie alcanza.

## Cómo se consume

El paquete se copia a `_identidad/` y se comprueba con las huellas. La copia es
la distribución, no una edición: si un archivo cambia, se actualiza el paquete.
La etiqueta se crea al fusionar el paquete; mientras no exista, el consumo queda
**Pendiente**, no verde.

```bash
base=https://raw.githubusercontent.com/lanuzalorenzo/lanuzalorenzo.github.io/identidad-v1.4.2/identidad
mkdir -p _identidad
for f in identidad.css plantilla.tpl shell.py menu.js marca-tile.svg SHA256SUMS VERSION LEEME.md; do
  curl -sSfL "$base/$f" -o "_identidad/$f"
done
(cd _identidad && sha256sum -c SHA256SUMS)
```

Con el paquete dentro, la página se compone así:

```python
from shell import Sitio

sitio = Sitio(perfil="publica", estilos=["_identidad/identidad.css", "sitio.css"],
              version="1", repo="https://github.com/…")
html = sitio.pagina(
    titulo="…", descripcion="…", canonical="https://…/",
    actual="index.html",
    contenido=cuerpo,
)
```

`contenido` se coloca dentro de `<main id="contenido">`. Un consumidor con
reparto propio pasa `cuerpo` —el bloque completo entre la cabecera y el pie— y
deja `contenido` fuera; los dos no se mezclan.

La marca de la cabecera y del pie enlaza siempre a la raíz del dominio (`/`),
también desde una web servida en un subdirectorio. Solo se pasa `inicio` cuando
el sitio no vive en la raíz.

La navegación también es del paquete: no se pasa `nav`. El consumidor indica
`actual` —`portfolio.html`, `api.html`, `biblioteca`…— y el paquete marca la
sección. El pie usa la nota y el enlace de código del paquete; no se reescriben.

Si el consumidor solo quiere las piezas, `Sitio.cabecera(nav=...)` y
`Sitio.pie(nota=...)` devuelven la cabecera y el pie con los mismos tokens y
condicionales; el consumidor aporta la nav y su distribución.

`ejemplo/` es el mismo caso completo, con `sitio.toml` y dos páginas. Se compila
con `python3 identidad/ejemplo/build.py`; `--check` compone sin escribir y
verifica que la plantilla, la nav y el perfil encajan.

## Lo que trae la capa

- **Marco de página** (`.frame`): ancho común con `--frame` como tope y márgenes
  laterales de 40 px, 24 px a 850 y 20 px a 620. Cada web coloca su contenido
  dentro; el reparto interno es suyo.
- **Cabecera y pie** ya compuestos, con la nav que recibe el consumidor.
- **Botones e insignias de estado**, con el color en el texto.
- **Tokens**: paleta, tipografía y alturas.

## Lo que no trae

Ni la gramática de página del portfolio, ni las filas de artefacto, ni la imagen
Open Graph, ni el juego completo de faviconos, ni las secciones de la portada,
ni la rejilla de un visor con lateral. Eso es de cada web.

## Lo que el paquete garantiza

- Un solo acento cian; `--accent-hover` es refuerzo del acento, no un segundo color.
- Ningún hex fuera de `:root`; los tonos nuevos se derivan con `color-mix`.
- El estado va en la insignia, una vez por fila, y el color tiñe el texto.
- Sin dependencias externas: ni CDN, ni fuentes, ni iconos por red.
- Nada de copiar y retocar: se consume una versión y se actualiza.
