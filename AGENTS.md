# Guía para agentes: web personal (lanuzalorenzo.github.io)

Sitio estático publicado con GitHub Pages. Presenta el perfil profesional completo —arquitectura de software, .NET, Azure, DevSecOps y Cloud Security— y enlaza el portfolio de ciberseguridad como un proyecto destacado.

## Contenido

- Es la fuente única de trayectoria, stack, formación y certificaciones. El README del perfil (`lanuzalorenzo`) es una tarjeta: si cambia el contenido largo, actualiza la web y deja en el README solo posicionamiento, proyectos y enlaces.
- Al cambiar módulos, prácticas, estados o enlaces del [portfolio](https://github.com/lanuzalorenzo/portfolio-ciberseguridad-lorenzo), revisa `#proyectos` y `#portfolio` y alinea los estados. «Runbook preparado» se muestra como «Diseño · runbook listo» y nunca como validado.
- Español claro y directo, sin rótulos de registro. Estados: Validado · Parcial · Runbook preparado · Diseño · Pendiente.
- Sin secretos, datos personales sensibles ni enlaces a repositorios privados.

## Convenciones visuales

- La paleta son las variables de `:root` en `styles.css`; fuera de la web los valores se escriben a mano.
- Las carpetas `assets/marca/`, `assets/iconos/` y `assets/social/` documentan sus piezas en su `README.md`.
- Iconos: 64×64, `rx=16`, fondo navy con degradado y glifo blanco relleno. Sin etiqueta, sin número y sin color por repositorio ni por módulo.
- Nada de dependencias externas para iconos ni diagramas: SVG en línea o archivos del propio repositorio.
- Conserva el diseño adaptable, la accesibilidad, la navegación por teclado y el soporte para movimiento reducido.

## Convenciones técnicas

- Sitio estático compatible con GitHub Pages.
- El workflow `.github/workflows/pages.yml` publica solo archivos públicos: `index.html`, `styles.css`, `app.js`, `assets`, faviconos, `.nojekyll`, `robots.txt` y `sitemap.xml`. Si añades un archivo público, inclúyelo en el paso de copia.
- `.github/CODEOWNERS` apunta a `@lanuzalorenzo`; los PR requieren su revisión y el bypass de administración queda limitado al propietario.
- Al cambiar contenido, actualiza `lastmod` en `sitemap.xml`.

## Commits

Formato: `type(scope): imperative summary in English`. Scopes: `site`, `repo`. Tipos: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`. Asunto imperativo, conciso y en inglés.
