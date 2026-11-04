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
- **Cian de señal** (`#38bdf8`): el único acento. Enlaces, bordes de control, estado activo y el punto de la marca. Sobre el fondo da 8,75:1.
- **Cian claro** (`#7dd3fc`): hover y enlaces sobre superficie. No es un segundo acento: es el mismo, iluminado.
- **Cian profundo** (`#0369a1`): bordes y degradados. Nunca texto pequeño: 3,16:1.

### Neutral
- **Navy de fondo** (`#07131e`): el plano. Toda la página.
- **Navy elevado** (`#0e2a47`): superficie de tarjetas y visuales.
- **Tinta** (`#f8fafc`): texto principal, 17,91:1 sobre el fondo.
- **Gris azulado** (`#a3b8c9`): texto secundario, 9,15:1 sobre el fondo.

### Estados (no son paleta)
- **Validado** (`#6ee7b7`), **Parcial** (`#fde68a`), **Diseño** (`#93c5fd`), **Pendiente** (`#cbd5e1`): solo dentro de una insignia. Nunca fondo de sección ni borde decorativo.

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
- **Insignias:** píldora de `999px` con el color de estado en texto, fondo al 12 % y borde al 30 %.

### Cards / Containers
- **Corner Style:** ninguna en ninguna tarjeta.
- **Background:** `surface` sobre `paper` y sobre `surface-deep`; `paper-deep` y `surface-deep` hacen de banda.
- **Shadow Strategy:** sin sombra. La profundidad la da el tono.
- **Border:** ninguno en proyecto y aptitud; 1 px `line` en la tarjeta de módulo.
- **Internal Padding:** 22–26 px en módulo y aptitud; 32–36 en la tarjeta de proyecto en escritorio.
- **Sobre la banda:** las tarjetas de proyecto y de aptitud se apoyan sobre `surface-deep`; la de módulo, sobre `paper`.

### Navigation
- **Style:** enlaces de 12 px y peso 650 en gris azulado. El activo va en tinta clara con una línea cian de 2 px sobre el borde del encabezado; sin subrayado de texto.
- **Mobile:** botón redondo de 44×44 que abre el menú; el foco se mantiene visible.

### Fila desplegable
- **Forma:** tres columnas —fecha, puesto, control— separadas por una línea de 1 px; a 620 quedan dos.
- **Estado:** el control redondo cambia de borde y el contenido se abre debajo sin mover la fila.
- **Uso:** trayectoria, módulos de portfolio y capacidades de la API comparten esta gramática.

## Do's and Don'ts

### Do:
- **Do** derivar cada tono nuevo con `color-mix` de los tokens y declararlo en `:root`.
- **Do** medir el contraste sobre el fondo real: 4,5:1 en texto, 3:1 en texto grande y bordes de control.
- **Do** dejar el antetítulo numerado: numera la sección y ordena la lectura.
- **Do** rematar el titular con Georgia itálica, en una parte corta.
- **Do** separar bloques con tono y línea antes que con una caja.

### Don't:
- **Don't** introducir un segundo acento ni un hex suelto.
- **Don't** redondear una tarjeta fuera de la de módulo ni poner un borde lateral de color.
- **Don't** bajar de 11 px un texto que informa.
- **Don't** quitar el contorno de foco.
- **Don't** poner texto con degradado, sombra de color difusa ni un halo por bloque.
- **Don't** usar el color de estado como superficie.
