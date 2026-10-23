# Guía para agentes: Web personal (lanuzalorenzo.github.io)

> **Si llegas nuevo:** el contrato de contenido es el de `portfolio-ciberseguridad-lorenzo/AGENTS.md`. Este archivo añade convenciones propias del sitio web.

Este repositorio contiene la web personal de Lorenzo Lanuza, publicada con GitHub Pages. Su objetivo es presentar el perfil profesional completo —arquitectura de software, .NET, Azure, DevSecOps y Cloud Security— y enlazar el portfolio de ciberseguridad como uno de varios proyectos destacados.

## Convenciones de contenido (compartidas con el portfolio)
- **Prohibido:** bloques «En fácil», «TL;DR», «En resumen» u otros rótulos de registro. Se escribe en español claro y directo.
- **Estados:** usa solo **Validado**, **Parcial**, **Runbook preparado**, **Diseño** o **Pendiente**. Un diseño o runbook sin ejecutar no es una validación.
- **Estructura:** este sitio es la fuente única de trayectoria, stack, formación y certificaciones. El README del perfil (`lanuzalorenzo`) es solo una tarjeta de presentación: al cambiar contenido largo, actualiza la web y deja en el README únicamente el posicionamiento, los proyectos y los enlaces.
- **Sincronización:** cuando cambien módulos, prácticas, estados o enlaces en `portfolio-ciberseguridad-lorenzo`, revisa las secciones `#proyectos` y `#portfolio` y mantén los estados alineados. «Runbook preparado» se muestra como «Diseño · runbook listo» y nunca como validado.
- No añadas secretos, datos personales sensibles ni enlaces a repositorios privados.
- Conserva el diseño adaptable, la accesibilidad, la navegación por teclado y el soporte para movimiento reducido.

## Convenciones técnicas
- Sitio estático compatible con GitHub Pages (sin dependencias externas para diagramas: SVG en línea).
- `.github/CODEOWNERS` apunta a `@lanuzalorenzo`; los PR requieren su revisión; bypass de administración limitado al propietario.
- El workflow `.github/workflows/pages.yml` publica solo archivos públicos (`index.html`, `styles.css`, `app.js`, `assets`, favicons, `.nojekyll`, `robots.txt`, `sitemap.xml`).
- Al cambiar contenido, actualiza `lastmod` en `sitemap.xml`.

## Convenciones de Commits
Formato: `type(scope): imperative summary in English`.
Ámbitos permitidos: `site`, `repo`.
Tipos permitidos: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.
El asunto debe ser imperativo, conciso y en inglés.