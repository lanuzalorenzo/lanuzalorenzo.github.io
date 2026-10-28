# Marca LL

Monograma del sitio: dos eles escalonadas, la primera blanca y la segunda cian, con el punto cian como ancla.

## Geometría

- Lienzo `viewBox="0 0 64 64"`, marca entre `(10,14)` y `(54,50)`.
- Primera L: `M10 14H18V42H26V50H10Z` en `#f8fafc`.
- Segunda L: `M30 24H38V42H54V50H30Z` en `#38bdf8`.
- Punto: círculo de radio 5 en `(42,17)`, `#38bdf8`, separado de la segunda L por 2 px de hueco.

## Ficheros

| Fichero | Uso | PNG |
|---|---|---|
| `marca-tile.svg` | Baldosa 64×64 con fondo degradado y borde cian. Es la versión del favicon | 16, 32, 64, 180 y 512 |
| `marca.svg` | Marca sola sobre fondo transparente, para superficies navy ya existentes | 16, 32, 64, 180 y 512 |
| `marca-mono.svg` | Una tinta `#f8fafc`, punto incluido | 16, 32, 64, 180 y 512 |

`marca.svg` y `marca-mono.svg` son de tinta clara: sobre fondo claro no se ven, y ahí se usa la baldosa. Los PNG se generan desde el SVG; el SVG es la fuente.

`favicon.svg` en la raíz del sitio es la misma pieza que `marca-tile.svg`, y `favicon.png` es su PNG a 180.

## El punto

Es lo único que no cambia entre versiones. Va siempre en el mismo sitio, en hueco abierto y separado de la segunda L: apoyado sobre el pie de la L se funde con ella y a 16 px desaparece, que es justo el fallo que tenía el favicon anterior. En la versión monocroma pierde el cian, no la posición.

## Lo que no se hace

- No se añaden degradados, sombras ni contornos nuevos.
- No se pone texto ni etiqueta dentro de la marca.
- No se separan las dos L para hacer una marca de tres iniciales: a 16 px no hay sitio y el conjunto deja de leerse.

La marca es propia y no procede de ninguna biblioteca de iconos.
