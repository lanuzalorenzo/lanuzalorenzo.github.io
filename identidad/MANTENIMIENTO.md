# Capa de identidad — mantenimiento

Este archivo es del repositorio dueño: no se distribuye con el paquete. El
contrato de consumo está en `LEEME.md`.

## La fuente es `styles.css`

El CSS del paquete no se retoca: se regenera desde `styles.css` de esta web.

```bash
python3 identidad/extraer.py          # reescribe identidad.css
# subir VERSION
python3 identidad/verificar.py --update
```

`identidad.css` copia las reglas de los selectores que son marca y descarta el
resto. Si una regla nueva de marca no aparece en la salida, se añade su selector
a `MARCA` en `extraer.py`; no se edita `identidad.css` a mano. Las at-rules se
recorren enteras y se conserva el bloque solo si queda alguna regla de marca
dentro, así que una regla nueva en `@media` o en `@supports` no se pierde.

## Qué comprueba `verificar.py`

Falla si `identidad.css` no coincide con `styles.css`, si la baldosa no es la de
`assets/marca/`, si `SHA256SUMS` no corresponde o si la versión de la cabecera no
es la de `VERSION`. `--update` reescribe las huellas y se niega a hacerlo si el
contenido cambió y `VERSION` sigue igual que en `HEAD`: una versión no puede
publicar dos contenidos.

`scripts/build.py --check` lo ejecuta, junto con el ejemplo, así que la deriva se
detecta antes de publicar.

## El ejemplo

`ejemplo/` es un sitio mínimo que usa el paquete y sirve de punto de partida.
Se compila con `python3 identidad/ejemplo/build.py`; `--check` compone sin
escribir. Vive con el dueño porque no forma parte del consumo.
