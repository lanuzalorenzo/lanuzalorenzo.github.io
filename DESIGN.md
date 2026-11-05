---
name: lanuzalorenzo.github.io
description: Perfil profesional de arquitectura de software, DevSecOps y Cloud Security
colors:
  paper: "#07131e"
  paper-deep: "#0e2a47"
  surface: "color-mix(in srgb, #0e2a47 72%, #07131e)"
  surface-deep: "color-mix(in srgb, #07131e 82%, #000)"
  ink: "#f8fafc"
  muted: "#a3b8c9"
  accent: "#38bdf8"
  accent-hover: "#7dd3fc"
  accent-dark: "#0369a1"
  line: "color-mix(in srgb, #38bdf8 16%, #0e2a47)"
  line-strong: "color-mix(in srgb, #38bdf8 60%, #0e2a47)"
  state-valid: "#6ee7b7"
  state-partial: "#fde68a"
  state-design: "#93c5fd"
  state-pending: "#cbd5e1"
typography:
  display:
    fontFamily: "Avenir Next, Avenir, Segoe UI, sans-serif"
    fontSize: "clamp(72px, 9.1vw, 122px)"
    fontWeight: 760
    lineHeight: 0.82
    letterSpacing: "-0.09em"
  section:
    fontFamily: "Avenir Next, Avenir, Segoe UI, sans-serif"
    fontSize: "clamp(36px, 4.6vw, 56px)"
    fontWeight: 680
    lineHeight: 1.02
    letterSpacing: "-0.07em"
  quote:
    fontFamily: "Georgia, Times New Roman, serif"
    fontStyle: italic
    fontWeight: 400
  lead:
    fontFamily: "Avenir Next, Avenir, Segoe UI, sans-serif"
    fontSize: "22px"
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: "-0.04em"
  body:
    fontFamily: "Avenir Next, Avenir, Segoe UI, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.65
  small:
    fontFamily: "Avenir Next, Avenir, Segoe UI, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Avenir Next, Avenir, Segoe UI, sans-serif"
    fontSize: "11px"
    fontWeight: 750
    letterSpacing: "0.15em"
  nav:
    fontFamily: "Avenir Next, Avenir, Segoe UI, sans-serif"
    fontSize: "12px"
    fontWeight: 650
    letterSpacing: "0em"
rounded:
  none: "0"
  tag: "4px"
  full: "50%"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
  "2xl": "32px"
  "3xl": "48px"
  "4xl": "64px"
components:
  button-primary:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0 19px"
    height: "48px"
  button-primary-hover:
    backgroundColor: "color-mix(in srgb, {colors.surface-deep} 82%, {colors.accent})"
  button-quiet:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0 19px"
    height: "48px"
  filter-button:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
  filter-button-active:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.paper}"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: "22px"
  nav-link:
    textColor: "{colors.muted}"
    typography: "{typography.nav}"
---

# Sistema visual: lanuzalorenzo.github.io

## Overview

**Idea rectora: "el plano de una instalación".**

La web se lee como la documentación de un sistema: fondo navy profundo, una sola tinta clara, un cian que señala lo activo y nada más, y líneas finas que ordenan sin decorar. No hay tarjetas flotantes ni superficies amables: hay bandas, separadores y una retícula que se ve. La densidad es alta y la jerarquía se construye con tamaño y espacio, no con color.

La marca aparece poco y siempre como firma: el retrato, el punto cian del estado, el monograma. El protagonismo lo lleva el contenido.

**Características clave:**
- Un solo tema, oscuro. No hay variante clara; la impresión es otra superficie y tiene su hoja.
- Un solo acento. El cian ilumina, no compite.
- El contenedor es recto; el radio se queda en etiquetas, píldoras y controles.
- Titular en sans con un remate en serif itálica: la parte que matiza.

## Colors

Paleta fría de dos profundidades y un acento cian. Todo lo demás se deriva con `color-mix`.

### Primary
- **Cian de señal** (`#38bdf8`): el único acento. Enlaces, bordes de control, enlace activo y el punto de la marca. Sobre el fondo da 8,75:1.
- **Cian claro** (`#7dd3fc`): hover y enlaces sobre superficie. No es un segundo acento: es el mismo, iluminado.
- **Cian profundo** (`#0369a1`): bordes y degradados. Nunca texto pequeño: 3,16:1.

### Neutral
- **Navy de fondo** (`#07131e`): el plano. Toda la página.
- **Navy elevado** (`#0e2a47`): superficie de tarjetas y visuales.
- **Tinta** (`#f8fafc`): texto principal, 17,91:1 sobre el fondo.
- **Gris azulado** (`#a3b8c9`): texto secundario, 9,15:1 sobre el fondo.

### Estados (no son paleta)
- **Validado** (`#6ee7b7`), **Parcial** (`#fde68a`), **Diseño** (`#93c5fd`), **Pendiente** (`#cbd5e1`): solo en el texto de la insignia de una fila. Nunca en fondos, bordes, títulos, contadores ni controles. «Runbook preparado» se muestra como «Diseño · runbook listo» y usa el color de Diseño.

### Reglas con nombre
**La regla del acento único.** El cian no se usa dos veces en el mismo bloque con dos funciones distintas. Si hay que distinguir algo más, se distingue con tamaño, peso o espacio.

**La regla del hex prestado.** Un color nuevo no se escribe: se deriva con `color-mix` de los tokens. Un hex suelto en el CSS es una fuga de la identidad.

## Typography

**Display y cuerpo:** Avenir Next, con Avenir y Segoe UI de reserva.
**Remate:** Georgia, con Times New Roman de reserva, siempre en itálica y solo dentro de un titular.

**Carácter:** la sans sostiene la lectura y da la voz técnica; la serif itálica introduce el matiz, como una nota al margen dentro de la frase.

### Hierarchy
- **Display** (760, `clamp(72px, 9.1vw, 122px)`, 0.82, -0.09em): titular de portada. Máximo dos líneas.
- **Section** (680, `clamp(36px, 4.6vw, 56px)`, 1.02, -0.07em): titular de sección.
- **Lead** (600, 22px, 1.5, -0.04em): primer párrafo, el que resume.
- **Body** (400, 15px, 1.65): prosa. Medida de 45–75 caracteres.
- **Small** (400, 12–14px): apoyo, notas, detalles de una fila.
- **Label** (750, 11px, 0.15em, caja alta): antetítulo, botón, índice, banda y rótulos del gráfico.

### Reglas con nombre
**La regla del suelo de 11 px.** Un texto que hay que leer no baja de 11 px; en móvil, de 12. Por debajo solo hay textura, y la textura se puede borrar sin perder nada.

**La regla del remate.** El titular empieza en sans y termina en serif itálica, nunca al revés y nunca entero en serif.

## Layout

Retícula de contenido de 1180 px, con 40 px de margen lateral en escritorio. Las secciones alternan tres tonos: `paper` en el plano, `paper-deep` en experiencia y `surface-deep` en proyectos. Separan bloques sin añadir cajas.

- El contenido se capa a 680 px entre 728 y 850 px de ancho; el margen lateral mínimo es 24 px, y 20 en móvil.
- A 900, la rejilla de proyectos pasa a una columna y cada tarjeta se parte en dos: texto y visual.
- A 850 el encabezado se estrecha y la portada mantiene dos columnas, con el gráfico más pequeño.
- A 620 la portada pasa a bloque y las rejillas de dos y tres columnas caen a una, salvo la de métricas, que se queda en tres.
- La fila de trayectoria pasa de tres columnas a dos a 620.
- El aire entre secciones va de 64 a 96 px; en móvil baja a 64–70.
- La proximidad agrupa antes que el borde: si dos cosas van juntas, se acercan.

## Elevation & Depth

No hay sombras difusas de color. La profundidad se construye por tono —`paper`, `paper-deep`, `surface` y `surface-deep`—, por anillos de 0 desenfoque en el retrato y el núcleo del gráfico, y por un halo radial de acento que aparece una vez por vista.

### Shadow Vocabulary
- **Anillo de retrato** (`0 0 0 7px paper, 0 0 0 8px color-mix(line 75%, transparent)`): separa la foto del fondo sin elevarla.
- **Anillo del núcleo** (`0 0 0 13px color-mix(accent 16%, transparent)`): marca el centro del gráfico.
- **Sombra de apoyo** (`0 22px 60px #020a12aa`): solo bajo el núcleo del gráfico, para despegarlo del halo.

### Regla con nombre
**La regla del halo único.** El halo radial de acento es la firma de profundidad y aparece una vez por vista. Sobre una tarjeta, es decoración.

## Shapes

El contenedor es recto: las bandas y las tarjetas de proyecto y de aptitud no llevan radio ni borde propio. El radio queda para lo pequeño:

- Etiqueta de módulo: `4px`.
- Píldora de estado, de proyecto o de capa: `999px`.
- Círculo: `50%` en retrato, punto de estado y control redondo.

Ninguna tarjeta lleva radio. Bordes de 1 px con `line` para separar; `line-strong` solo cuando el borde delimita un control y necesita 3:1. Sin tarjeta dentro de tarjeta. Los rótulos del gráfico son textura: no llevan un dato que no esté en la tarjeta y no bajan de 11 px.

## Components

### Buttons
- **Forma:** recta, sin radio; 48 px de alto y 19 px de relleno lateral.
- **Primary:** superficie hundida, tinta clara, etiqueta de 11 px en caja alta. Se eleva 2 px al pasar el ratón.
- **Quiet:** transparente con borde `line-strong`; al pasar el ratón, superficie elevada.
- **Hover / Focus:** el foco es un contorno de 2 px en cian con 4 px de separación. Nunca se quita.

### Chips
- **Style:** filtro recto de 11 px, borde `line-strong`, texto secundario.
- **State:** activo en cian sólido con texto navy.
- **Insignias:** píldora de `999px`, fondo transparente y borde `line`; el color de estado va solo en el texto. Detalle en «El estado».

### Cards / Containers
- **Corner Style:** ninguna en ninguna tarjeta.
- **Background:** `surface` sobre `paper` y sobre `surface-deep`; `paper-deep` y `surface-deep` hacen de banda.
- **Shadow Strategy:** sin sombra. La profundidad la da el tono.
- **Border:** ninguno en proyecto y aptitud. La tarjeta de módulo se retiró al aplicar la fila tipo; no se documenta como componente vigente.
- **Internal Padding:** 32–36 px en la tarjeta de proyecto en escritorio; 22–26 en aptitud.
- **Sobre la banda:** las tarjetas de proyecto y de aptitud se apoyan sobre `surface-deep`.

### Navigation
- **Style:** enlaces de 12 px y peso 650 en gris azulado. El activo va en tinta clara con una línea cian de 2 px sobre el borde del encabezado; sin subrayado de texto.
- **Mobile:** botón redondo de 44×44 que abre el menú; el foco se mantiene visible.

### Fila de trayectoria
- **Forma:** tres columnas —fecha, puesto, control— separadas por una línea de 1 px; a 620 quedan dos.
- **Estado:** el control redondo cambia de borde y el contenido se abre debajo sin mover la fila.
- **Uso:** solo la trayectoria de la portada. Las páginas de artefacto usan la fila tipo descrita en «Fila tipo».

## Gramática de página

**Alcance.** Esta gramática es la de las tres páginas de detalle: `portfolio.html`, `api.html` e `ia.html`. Las tres usan ya la fila de artefacto. La portada (`index.html`) conserva su secuencia propia —hero, ticker, perfil, experiencia, proyectos y contacto— y no adopta esa fila: sus tarjetas de proyecto no declaran estado.

**Secuencia de bloques.** Las tres páginas se leen en el mismo orden:

1. **Cabecera de página.** `section-heading`: antetítulo, `h1` de dos líneas con remate en serif y `portfolio-intro` con medida de 62 caracteres. El intro dice qué contiene la página y qué significa ahí el estado; si hay página hermana, la enlaza.
2. **Barra de control.** `portfolio-controls`: a la izquierda el total en prosa; a la derecha «Desplegar todos». El total cuenta grupos y filas, nunca estados.
3. **Familia.** `lab-label` solo cuando la página mezcla dos naturalezas de artefacto. `ia.html` lo usa para separar «Guías» de «Resultados y límites».
4. **Grupo.** `details.module-group` por tipo, familia, capa o tema. El `summary` lleva punto de apertura, título del grupo, número de filas y control `+ / −`. El título nombra el tipo, familia, capa o tema, nunca un estado.
5. **Filas.** `spec-table` con una `spec-row` por artefacto. La fila es la unidad de lectura y la única que declara estado.
6. **Cierre.** `portfolio-cta` con dos enlaces: el repositorio y la fuente completa de la página —guía de lectura, tabla de estado o hoja de ruta.

**Lo que se repite.** La cabecera, la barra de control, el `summary` de grupo, la fila, la insignia y el cierre; el ancho de 1180 px, el paso vertical entre secciones y los cortes de 850 y 620 px. Cambia el contenido —títulos, nombres, enlaces y estados—, no la forma.

**Lo que no se repite.** Ni una tarjeta por artefacto, ni un contador por estado, ni una insignia en el título del grupo, ni una insignia de más en la fila, ni un color de estado fuera de su insignia.

**Orden dentro del grupo.** Por número de módulo, por fecha del experimento o por el orden del control en su fuente. Nunca por estado: el estado no ordena ni filtra.

**Tipo y estado pueden coincidir.** Que hoy todos los resultados estén validados o parciales, y todos los límites en diseño o pendiente, no convierte «Resultados» en un grupo por estado. El criterio es la naturaleza del artefacto o el tema; si un grupo solo se puede nombrar con un estado, no es un grupo.

**El tono no forma parte de la gramática.** `portfolio.html` puede mantener `surface-deep` y `api.html` e `ia.html` el fondo `paper`; lo común es la estructura, no la banda de color.

### Estado actual

| Página | Agrupa por | Fila | Estado | Contenido |
|---|---|---|---|---|
| `portfolio.html` | capa del modelo (5 grupos) | `spec-row` | insignia, una vez | 12 módulos |
| `api.html` | familia de control (5 grupos) | `spec-row` | insignia, una vez | 28 controles y límites |
| `ia.html` | guías por trabajo y resultados o límites por tema (7 grupos) | `spec-row` | insignia, una vez | 9 guías y 11 resultados y límites |

## El estado

**Una fila, una insignia.** El estado se declara una vez y en un solo sitio: la insignia de la fila. No aparece en el antetítulo, en el `h1`, en el título del grupo, en el contador, en la barra de control, en el cierre ni en una segunda insignia.

**Los cinco estados.** Validado · Parcial · Runbook preparado · Diseño · Pendiente. «Runbook preparado» se muestra como «Diseño · runbook listo» y nunca como validado. Los matices —«en CI», «en local», «en plantilla», «documental», «+ IaC»— van en el texto de la insignia y no crean un estado nuevo.

| Estado | Clase | Token | Etiquetas que se ven hoy |
|---|---|---|---|
| Validado | `status-validated` | `--state-valid` | `Validado`, `Validado en CI`, `Validado en local`, `Validado · documental` |
| Parcial | `status-partial` | `--state-partial` | `Parcial`, `Parcial · local`, `Parcial · PIM`, `Parcial · plantilla` |
| Runbook preparado | `status-design` | `--state-design` | `Diseño · runbook listo` |
| Diseño | `status-design` | `--state-design` | `Diseño`, `Diseño + IaC` |
| Pendiente | `status-pending` | `--state-pending` | `Pendiente`, `Fuera de alcance` |

**La clase fija el estado; la etiqueta no lo deduce.** `Validado en local` se queda en Validado; la clase Parcial usa `Parcial · local`. No se promueve ni degrada ningún estado por la etiqueta. «Fuera de alcance» es la forma de Pendiente cuando el límite es de alcance, no trabajo que falte. La insignia no promete más que la fila.

**El color, solo en el texto.** La insignia tiene fondo transparente y borde `line`; el color de estado tiñe la etiqueta, no la caja. No hay estado en el fondo de una sección, en el borde de una fila, en el punto de un grupo, en un título ni en una barra. El color es refuerzo: el texto es el dato y el que lee un lector de pantalla.

**La insignia.** Píldora de `999px`, borde de 1 px en `line`, `3px 8px`, etiqueta de 11 px en escritorio y 12 px a 620, en caja alta y peso 700, `white-space: nowrap`. El contraste se mide sobre la superficie real, 4,5:1 mínimo. No lleva icono propio ni cambia de forma entre páginas.

**Estados compuestos.** Un texto que une dos estados —una validación con PIM parcial, por ejemplo— no lleva dos insignias ni el color del estado más alto. Se parte en dos filas si cada estado tiene evidencia propia, o se queda con el estado más bajo y el matiz en el texto.

## Fila tipo

La misma fila sirve a `portfolio.html`, `api.html` e `ia.html`. No hay tarjeta de módulo, caja por control ni rejilla de resultados: la página es una lista de grupos y cada grupo, una lista de filas.

| Campo | Obligatorio | Qué lleva | Dónde |
|---|---|---|---|
| Nombre | Sí | El artefacto en una frase, con el número de módulo delante en portfolio (`01 · Seguridad en Azure`). | En portfolio, `h2.spec-name`; en API e IA, `span.spec-name`. |
| Detalle | No | Una línea de contexto, una o dos, sin estado. | `.spec-detail` |
| Estado | Sí | Una insignia, la única de la fila. | `.module-status` + `.status-*` |
| Evidencia | Sí | Enlace al artefacto con su nombre corto y `↗`; si no hay, `Sin evidencia` visible. | `.module-link`; si falta, `.spec-none` |

```html
<div class="spec-row" role="listitem">
  <div class="spec-copy">
    <h2 class="spec-name">01 · Seguridad en Azure</h2>
    <span class="spec-detail">OAuth 2.0 con PKCE, JWT y JWKS.</span>
  </div>
  <span class="module-status status-partial">Parcial</span>
  <a class="module-link" href="…">Ver módulo ↗</a>
</div>
```

En API e IA, el nombre es `span.spec-name` y no lleva detalle; la fila conserva las mismas columnas.

- **Escritorio:** tres columnas `minmax(0, 1fr) auto minmax(0, 13rem)`, 18 px de hueco, 11 px arriba y abajo, línea inferior al 55 % de `line`. La primera fila no lleva borde superior.
- **A 850 px:** dos columnas; el nombre ocupa las dos, la insignia queda a la izquierda y la evidencia a la derecha en la segunda línea.
- **A 620 px:** igual, con el contador de grupo oculto.
- **La fila no se mueve al abrir o cerrar el grupo:** el `details` abre debajo y la fila conserva su sitio.
- **El grupo** lleva el tipo en el título, el número de filas en el contador y el punto de apertura en cian cuando está abierto. El punto no es un estado.
- **La evidencia ausente** se escribe, no se esconde: `Sin evidencia` con el mismo tamaño que el enlace y sin `aria-hidden`.

## La regla de `ia.html`

`ia.html` tiene dos familias y siete grupos. Arriba, bajo `lab-label` «Guías», cuatro grupos por trabajo: Montar el entorno (3), Trabajar con el agente (3), Decidir qué sale de la red (2) y Cuando algo falla (1). Debajo, bajo «Resultados y límites», tres grupos por tema: Entorno y uso (4), Instrumento y robustez (4) y Límites y alcance (3). Los grupos se definen por tema, no por estado; unos mezclan estados y otros no. El estado aparece una sola vez, en la insignia de cada fila. La barra de control cuenta 9 guías y 11 resultados y límites, sin nombrar estados. La página sigue siendo una página menor, no un tercer pilar.

## Do's and Don'ts

### Do:
- **Do** derivar cada tono nuevo con `color-mix` de los tokens y declararlo en `:root`.
- **Do** medir el contraste sobre el fondo real: 4,5:1 en texto, 3:1 en texto grande y bordes de control.
- **Do** dejar el antetítulo: numera la sección en la portada y nombra la página en las páginas de detalle.
- **Do** rematar el titular con Georgia itálica, en una parte corta.
- **Do** separar bloques con tono y línea antes que con una caja.
- **Do** declarar el estado una vez, en la insignia de la fila.
- **Do** agrupar por tipo, familia, capa o tema, y ordenar por número, fecha o fuente.
- **Do** usar la misma fila en portfolio, API e IA.

### Don't:
- **Don't** introducir un segundo acento ni un hex suelto.
- **Don't** poner el estado en títulos, contadores, fondos o bordes.
- **Don't** convertir el estado en criterio de agrupación u orden.
- **Don't** añadir una segunda insignia ni una tarjeta por artefacto.
- **Don't** redondear una tarjeta ni poner un borde lateral de color.
- **Don't** bajar de 11 px un texto que informa.
- **Don't** quitar el contorno de foco.
- **Don't** poner texto con degradado, sombra de color difusa ni un halo por bloque.
- **Don't** usar el color de estado como superficie.
