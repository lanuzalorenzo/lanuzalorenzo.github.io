# Marca LL

Monograma del sitio: dos eles escalonadas, la primera blanca y la segunda cian, con el punto cian como ancla.

## Geometría

- Lienzo `viewBox="0 0 64 64"`; las dos L van entre `(10,14)` y `(54,50)` y el punto llega hasta `y=11`.
- Primera L: `M10 14H18V42H26V50H10Z` en `#f8fafc`.
- Segunda L: `M30 24H38V42H54V50H30Z` en `#38bdf8`.
- Punto: círculo de radio 5 en `(42,16)`, `#38bdf8`, separado de la segunda L por 3 px de hueco vertical (0,75 px a 16, que se rasteriza como 1 px).

## Ficheros

| Fichero | Uso | PNG |
|---|---|---|
| `marca-tile.svg` | Baldosa 64×64 con fondo degradado y borde cian sólido de 2 px (`#38bdf8`, sin degradado ni opacidad). Es la versión del favicon y del icono de cabecera y pie | 16, 32, 64, 180 y 512 |
| `marca.svg` | Marca sola sobre fondo transparente, para superficies navy ya existentes | 16, 32, 64, 180 y 512 |
| `marca-mono.svg` | Una tinta `#f8fafc`, punto incluido | 16, 32, 64, 180 y 512 |
| `apple-touch-icon.png` | Icono de iOS, 180×180 opaco: tile de 162 px centrado sobre navy, sin transparencia | 180 |
| `favicon-16.svg` / `favicon-16.png` | Variante de 16 px para la pestaña: borde cian de 1 px sólido y hueco de 1 px; a 32+ se usa el tile normal | 16 |

`marca.svg` y `marca-mono.svg` son de tinta clara: sobre fondo claro no se ven, y ahí se usa la baldosa. Los PNG se generan desde el SVG; el SVG es la fuente.

`favicon.svg` en la raíz del sitio es la misma pieza que `marca-tile.svg`, y `favicon.png` es su PNG a 180. Para 16 px se sirve `favicon-16.png`, que mantiene el borde de 1 px y el hueco de 1 px; `favicon.svg` sigue siendo la misma pieza que `marca-tile.svg` para 32+. `apple-touch-icon.png` es la variante opaca para iOS: el tile baja a 162 px sobre un fondo navy para que la máscara de iOS no recorte el borde.

## El punto

Es lo único que no cambia entre versiones. Va siempre en el mismo sitio, en hueco abierto y separado de la segunda L: a 16 px se mantiene separado por 1 px. El fallo del favicon anterior era que el punto se fundía con la L y desaparecía; esa es la condición que no se puede repetir. En la versión monocroma pierde el cian, no la posición.

## Lo que no se hace

- No se añaden degradados, sombras ni contornos nuevos.
- No se pone texto ni etiqueta dentro de la marca.
- No se separan las dos L para hacer una marca de tres iniciales: a 16 px no hay sitio y el conjunto deja de leerse.

La marca es propia y no procede de ninguna biblioteca de iconos.
