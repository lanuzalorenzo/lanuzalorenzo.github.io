# Guía del repositorio

Este repositorio contiene la web personal de Lorenzo Lanuza, publicada con GitHub Pages. Su objetivo es presentar el perfil profesional completo —arquitectura de software, .NET, Azure, DevSecOps y Cloud Security— y enlazar el portfolio de ciberseguridad como uno de varios proyectos destacados.

Al trabajar en el repositorio:

- Conserva el enfoque de presentación profesional general; el sitio no debe convertirse en una página dedicada únicamente a ciberseguridad.
- Comprueba el contenido existente antes de cambiar la estructura o añadir dependencias. El sitio debe seguir siendo estático y compatible con GitHub Pages, salvo que se solicite expresamente otro enfoque.
- Este sitio es la fuente única de trayectoria, stack, formación y certificaciones. El README del perfil (`lanuzalorenzo`) es solo una tarjeta de presentación: al cambiar contenido largo, actualiza la web y deja en el README únicamente el posicionamiento, los proyectos y los enlaces.
- Si hubo varios periodos en una misma empresa o cliente, represéntalos como puestos separados con sus fechas y funciones propias; no los combines en una sola experiencia.
- No inventes experiencia, resultados, certificaciones ni validaciones. Distingue la experiencia profesional de los proyectos personales y laboratorios.
- Mantén los estados, módulos y enlaces alineados con `portfolio-ciberseguridad-lorenzo`. «Runbook preparado» se muestra como «Diseño · runbook listo» y nunca como validado.
- No añadas secretos, datos personales sensibles ni enlaces a repositorios privados.
- Conserva el diseño adaptable, la accesibilidad, la navegación por teclado y el soporte para movimiento reducido.
- Verifica las interacciones y los enlaces afectados al modificar filtros, navegación, tema o contenido de proyectos.
- Mantén `.github/CODEOWNERS` apuntando a `@lanuzalorenzo`; los PR de colaboradores deben requerir su revisión y el bypass de administración debe quedar limitado al propietario.
- Escribe la interfaz y la documentación en español claro; conserva los nombres oficiales de tecnologías y certificaciones.

## Sincronización y crecimiento

- Cuando cambien módulos, prácticas, estados o enlaces en `portfolio-ciberseguridad-lorenzo`, revisa las secciones `#proyectos` y `#portfolio` y mantén los estados alineados.
- La sección `#portfolio` enlaza la guía de lectura del portfolio (`docs/guia-de-lectura.md`); si cambia su URL o el nombre del archivo, actualiza el botón «Guía de lectura».
- Mantén el sitio como una página estática y ligera mientras el contenido sea manejable. Si crece, usa subpáginas dentro del mismo dominio (`/portfolio/...`, `/labs/...`) con los mismos estilos y assets.
- Reserva una GitHub Page satélite independiente solo para una aplicación web funcional interactiva; la documentación y los laboratorios se quedan en el dominio principal o en los README de GitHub.

## Convenciones de Commits

Todos los commits de este repositorio, realizados por el usuario o por asistentes de IA, deben seguir estrictamente **Conventional Commits**:

- Formato: `type(scope): imperative summary in English`.
- **Ámbitos (`scope`) permitidos:** `site`, `repo`.
- **Tipos permitidos:** `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.
- El asunto debe ser conciso, imperativo y redactado en inglés.
- Ejemplos:
  - `feat(site): add interactive project filters`
  - `fix(site): improve mobile navigation behavior`
  - `docs(repo): explain GitHub Pages deployment`
