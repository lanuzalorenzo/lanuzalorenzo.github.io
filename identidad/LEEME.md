# Capa de identidad

Cabecera, pie, navegación, botones, insignias y tokens de la marca, en un paquete
que otra web consume tal cual. Se separa en dos piezas: el CSS con los valores y
la plantilla con el marcado. Cada web pone su contenido y su distribución; no
rehace la cabecera.

## Qué hay

| Archivo | Qué es |
|---|---|
| `identidad.css` | Tokens, tipografía base, cabecera y nav, pie, botones, insignias, foco y movimiento reducido |
| `plantilla.tpl` | Shell con marcadores `{{...}}` y bloques por perfil |
| `shell.py` | Compone una página con la plantilla: perfiles, nav, metadatos y comprobación de marcadores |
| `menu.js` | Abrir y cerrar el menú en móvil; sin dependencias |
| `marca-tile.svg` | La baldosa de la marca, la misma que sirve la web |
| `SHA256SUMS` | Huellas de los cinco archivos anteriores |
| `VERSION` | Versión del paquete; `identidad.css` la declara en su cabecera |
| `extraer.py` | Genera `identidad.css` desde `styles.css`; no se edita el CSS a mano |
| `verificar.py` | Comprueba que el paquete está al día; `--update` reescribe las huellas |
| `ejemplo/` | Sitio mínimo que usa el paquete; sirve de punto de partida |

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
base=https://raw.githubusercontent.com/lanuzalorenzo/lanuzalorenzo.github.io/identidad-v1.0.0/identidad
mkdir -p _identidad
for f in identidad.css plantilla.tpl shell.py menu.js marca-tile.svg SHA256SUMS VERSION; do
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
    nav=[("#perfil", "Perfil"), {"grupo": "Proyectos"}, ("api.html", "API")],
    actual="index.html", contenido=cuerpo,
)
```

`ejemplo/` es el mismo caso completo, con `sitio.toml` y dos páginas. Se compila
con `python3 identidad/ejemplo/build.py`; `--check` compone sin escribir y
verifica que la plantilla, la nav y el perfil encajan.

## Cómo se actualiza

La fuente es `styles.css` de esta web. El CSS del paquete no se retoca: se
regenera.

```bash
python3 identidad/extraer.py          # reescribe identidad.css
# subir VERSION
python3 identidad/verificar.py --update
```

`verificar.py` falla si `identidad.css` no coincide con `styles.css`, si la
baldosa no es la de `assets/marca/`, si `SHA256SUMS` no corresponde o si la
versión de la cabecera no es la de `VERSION`. `--update` se niega a reescribir
las huellas si el contenido cambió y `VERSION` sigue igual que en `HEAD`: una
versión no puede publicar dos contenidos. `scripts/build.py --check` lo ejecuta,
junto con el ejemplo, así que la deriva se detecta antes de publicar.

## Lo que no trae

Ni la gramática de página del portfolio, ni las filas de artefacto, ni la imagen
Open Graph, ni el juego completo de faviconos, ni las secciones de la portada.
Eso es de cada web. Tampoco trae la regla de marca: los valores están aquí, la
regla vive con su dueño.

## Lo que el paquete garantiza

- Un solo acento cian; `--accent-hover` es refuerzo del acento, no un segundo color.
- Ningún hex fuera de `:root`; los tonos nuevos se derivan con `color-mix`.
- El estado va en la insignia, una vez por fila, y el color tiñe el texto.
- Sin dependencias externas: ni CDN, ni fuentes, ni iconos por red.
- Nada de copiar y retocar: se consume una versión y se actualiza.
