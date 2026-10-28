# Identidad visual del workspace

Una sola identidad para todo: la web, los README de los repositorios, los iconos y el escritorio. La referencia es el favicon del sitio, que ya aplicaba esta receta.

Este documento manda sobre cualquier pieza gráfica nueva. Si algo no encaja aquí, no es de la identidad.

## Paleta

| Rol | Valor |
|---|---|
| Fondo profundo | `#07131e` |
| Fondo elevado | `#0e2a47` |
| Texto / forma principal | `#f8fafc` |
| Acento | `#38bdf8` |
| Acento claro | `#7dd3fc` |
| Acento profundo | `#0369a1` |
| Texto secundario | `#a3b8c9` |

En la web estos valores son las variables de `:root` en `styles.css` (`--paper`, `--ink`, `--accent`, `--muted`). Fuera de la web se escriben a mano, porque un SVG servido dentro de `<img>` no hereda CSS ni variables.

## Iconos

Formato único, 64×64:

- Lienzo `viewBox="0 0 64 64"` con `rx="16"`.
- Fondo: degradado `#07131e` → `#0e2a47` en diagonal.
- Borde: 2 px con degradado `#38bdf8` (85 %) → `#0369a1` (50 %).
- Glifo: relleno `#f8fafc`, caja de 44×44 en `translate(10 10) scale(1.83334)`.
- Si el icono lleva distintivo: glifo principal de 36×36 en `translate(14 12) scale(1.5)` y distintivo de 14 px en un círculo de radio 12,5 centrado en `(49 49)`.
- Sin texto, sin número, sin etiqueta dentro del icono.

Reglas que no se negocian:

- **Relleno, no trazo.** Un trazo de 1,6 px a 64 se convierte en 0,8 px a 32 y desaparece. El trazo fino es recurso de los diagramas grandes de la web, no de los iconos.
- **Sin color por repositorio ni por módulo.** Todo es navy y cian. La distinción va en el glifo y en la etiqueta.
- **Una sola pieza por icono.** Nada de sellos, bandas, insignias ni rótulos.
- El cian vive en el borde y en el distintivo, no en el glifo principal. La única excepción es la marca LL, que es de dos tonos porque así está en el favicon.
- **Distintivo = contexto, no marca.** El globo significa «esto es un enlace web»; una marca pequeña significa «esto vive en ese servicio». Nunca dos marcas compitiendo.
- El glifo tiene que distinguirse a 32 px. Si a ese tamaño se confunde con otro de la familia, se cambia el glifo, no se le añade texto.

## Marcas de tecnología

Cuando el icono representa una tecnología concreta, vale su marca en lugar de un glifo genérico: `.NET` en la API, `Ollama` en el laboratorio de IA, `GitHub` en el perfil.

- Se toman de [Simple Icons](https://simpleicons.org/) (CC0) y se usan **sin modificar**, en blanco.
- Son marcas de sus titulares; se usan para identificar el proyecto, no para sugerir respaldo.
- Si la marca es un logotipo con texto, no se usa como glifo: a 44 px el texto desaparece. En ese caso se usa un glifo o la marca propia y el distintivo adecuado.

## Dónde vive cada pieza

| Superficie | Fuente única | Cómo se usa |
|---|---|---|
| Repositorios | `assets/iconos/` de cada repo | `<img width="64">` en la cabecera del README; `width="32"` en tablas |
| Web | `assets/iconos/` y SVG en línea | Los diagramas de proyecto siguen el mismo navy/cian con trazo fino |
| Escritorio | El `assets/iconos/` de cada repo | Las entradas `.desktop` apuntan ahí; no se guardan copias |

Los repositorios privados guardan sus iconos en `privatenotes/scripts/escritorio/iconos/` porque no publican `assets/`.

## Lo que no se puede

- GitHub no permite iconos por carpeta en el árbol de archivos ni fuentes propias en los README. La identidad en GitHub se aplica en el icono y en los badges, no en la tipografía.
- En un SVG dentro de `<img>` no hay `currentColor`, ni tema claro/oscuro, ni `prefers-color-scheme` fiable. Por eso el icono lleva su propio fondo y funciona igual sobre GitHub claro y oscuro.

## Añadir un icono

1. Elige un glifo de [Material Design Icons](https://pictogrammers.com/library/mdi/) (Apache 2.0) o la marca de [Simple Icons](https://simpleicons.org/) (CC0) y monta el SVG con la receta de arriba.
2. Guárdalo en el `assets/iconos/` del repo con un nombre que lo identifique; el icono no lleva texto.
3. Añádelo al `README.md` de esa carpeta y, si es un repo, a la cabecera del README.
