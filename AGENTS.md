# Guía del repositorio

Este repositorio contiene la web personal de Lorenzo Lanuza, publicada con GitHub Pages. Su objetivo es presentar el perfil profesional completo —arquitectura de software, .NET, Azure, DevSecOps y Cloud Security— y enlazar el portfolio de ciberseguridad como uno de varios proyectos destacados.

Al trabajar en el repositorio:

- Conserva el enfoque de presentación profesional general; el sitio no debe convertirse en una página dedicada únicamente a ciberseguridad.
- Comprueba el contenido existente antes de cambiar la estructura o añadir dependencias. El sitio debe seguir siendo estático y compatible con GitHub Pages, salvo que se solicite expresamente otro enfoque.
- Mantén coherentes la versión web y el README del perfil cuando cambien la experiencia, formación, certificaciones o enlaces.
- No inventes experiencia, resultados, certificaciones ni validaciones. Distingue la experiencia profesional de los proyectos personales y laboratorios.
- No añadas secretos, datos personales sensibles ni enlaces a repositorios privados.
- Conserva el diseño adaptable, la accesibilidad, la navegación por teclado y el soporte para movimiento reducido.
- Verifica las interacciones y los enlaces afectados al modificar filtros, navegación, tema o contenido de proyectos.
- Escribe la interfaz y la documentación en español claro; conserva los nombres oficiales de tecnologías y certificaciones.

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
