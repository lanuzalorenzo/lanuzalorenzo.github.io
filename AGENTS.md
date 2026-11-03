# Guía para agentes: web personal (lanuzalorenzo.github.io)

Sitio estático publicado con GitHub Pages. Presenta el perfil profesional completo —arquitectura de software, .NET, Azure, DevSecOps y Cloud Security— y enlaza el portfolio de ciberseguridad como un proyecto destacado.

## Contenido

- Es la fuente única de trayectoria, stack, formación y certificaciones. El README del perfil (`lanuzalorenzo`) es una tarjeta: si cambia el contenido largo, actualiza la web y deja en el README solo posicionamiento, proyectos y enlaces.
- Al cambiar módulos, prácticas, estados o enlaces del [portfolio](https://github.com/lanuzalorenzo/portfolio-ciberseguridad-lorenzo), revisa `#proyectos` y `#portfolio` y alinea los estados. «Runbook preparado» se muestra como «Diseño · runbook listo» (= `Runbook preparado`) y nunca como validado.
- `#api` es la sección hermana de `#portfolio`: misma gramática (grupos desplegables, estado por fila, enlace a la evidencia) y densidad de tabla. Su fuente es la matriz de `lab-api-local-azure/docs/capacidades.md`; la web lleva una selección de los controles principales y enlaza al resto. El contador visible se mantiene en la sección; si cambia el estado en el repo, sincroniza la sección en la misma sesión.
- `#ia` es una sección menor, no un tercer pilar: la unidad es el experimento, no el control, y se agrupa en Medido · Probado sin registro reproducible · Preparado y pendiente, que equivalen a Validado · Parcial · Diseño/Pendiente; no son estados nuevos. Su fuente es el README de `lab-ia-aprendizaje` y sus evidencias fechadas; no se le añaden filas sin evidencia en el repo.
- El estándar editorial completo —español claro, apertura llana, jerga y claridad que no cambia lo que se afirma— está en el [contrato del portfolio](https://github.com/lanuzalorenzo/portfolio-ciberseguridad-lorenzo/blob/main/AGENTS.md). En esta web: estados explícitos (Validado · Parcial · Runbook preparado · Diseño · Pendiente), sin secretos, datos personales sensibles ni enlaces a repositorios privados.

## Convenciones visuales

- La paleta son las variables de `:root` en `styles.css`; fuera de la web los valores se escriben a mano.
- Las carpetas `assets/marca/`, `assets/iconos/` y `assets/social/` documentan sus piezas en su `README.md`.
- Nada de dependencias externas para iconos ni diagramas: SVG en línea o archivos del propio repositorio.
- Conserva el diseño adaptable, la accesibilidad, la navegación por teclado y el soporte para movimiento reducido.

## Convenciones técnicas

- Sitio estático compatible con GitHub Pages.
- El workflow `.github/workflows/pages.yml` publica solo archivos públicos: `index.html`, `styles.css`, `app.js`, `assets`, faviconos, `.nojekyll`, `robots.txt` y `sitemap.xml`. Si añades un archivo público, inclúyelo en el paso de copia.
- `.github/CODEOWNERS` apunta a `@lanuzalorenzo`; `main` exige PR, el check de verificación y rama actualizada; solo el propietario fusiona.
- Al cambiar contenido, actualiza `lastmod` en `sitemap.xml`.

## Verificación

```bash
python3 scripts/check_links.py
gitleaks detect --source . --redact --verbose --exit-code 2
```

Son los dos checks del trabajo `verify` de `.github/workflows/pages.yml`: enlaces relativos y secretos sobre el historial completo. El despliegue solo ocurre tras ese trabajo.

## Commits

Formato: `type(scope): imperative summary in English`. Scopes: `site`, `repo`. Tipos: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`. Asunto imperativo, conciso y en inglés.
