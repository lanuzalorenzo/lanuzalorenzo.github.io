<img src="assets/iconos/web.svg" width="64" alt="Icono de la web personal">

# Web personal — Lorenzo Lanuza

Sitio estático de presentación profesional, experiencia, especialidades y proyectos. Los dos laboratorios —seguridad cloud sobre la API y AI Agent Local Lab— se presentan como proyectos destacados, no como tema principal. Los diagramas de cada proyecto son SVG en línea, sin dependencias externas.

## Contenido

- **Perfil y trayectoria:** experiencia profesional, formación y certificaciones.
- **Especialidades:** arquitectura, DevSecOps y Cloud Security.
- **Proyectos:** laboratorio de seguridad cloud (portfolio + `EcommerceApi`) y AI Agent Local Lab.
- **Portfolio de ciberseguridad:** doce módulos y un laboratorio final con siete evidencias indexadas (tres de ejecución, cuatro documentales o verificables).
- **La carga de trabajo (`EcommerceApi`):** el estado real de 28 controles y límites —seguridad, pruebas, datos, CI y alcance declarado— con enlace a la evidencia de cada uno.
- **Contacto y CV:** enlaces profesionales y PDF optimizado para ATS.

## Publicar en GitHub Pages

1. Crea un repositorio público llamado exactamente `lanuzalorenzo.github.io` en la cuenta `lanuzalorenzo`.
2. Desde esta carpeta, publica los archivos en la rama `main`:

   ```bash
   git add .
   git commit -m "feat(site): create personal portfolio website"
   git push -u origin main
   ```

3. En GitHub, abre **Settings → Pages** y selecciona **GitHub Actions** como origen de publicación.
4. El workflow de `.github/workflows/pages.yml` desplegará el sitio. La dirección será `https://lanuzalorenzo.github.io/`.

Cada `push` a `main` volverá a publicar la web. El workflow copia a `_site` solo los archivos públicos del sitio (`index.html`, `styles.css`, `app.js`, `assets`, favicons, `.nojekyll`, `robots.txt` y `sitemap.xml`), de modo que la documentación interna y el historial de Git no forman parte del artefacto. Al cambiar el contenido, actualiza `lastmod` en `sitemap.xml`.

El botón **Descargar CV** entrega el PDF real alojado en `assets/cv/lanuza-lorenzo-cv.pdf` (CV de 2 páginas optimizado para ATS), no una copia impresa de la página. Para actualizarlo, reemplaza ese fichero manteniendo el mismo nombre: la URL no cambia y los enlaces ya compartidos siguen funcionando.

## Protección de la rama `main`

`.github/CODEOWNERS` asigna la revisión del código a `@lanuzalorenzo`. Para exigir que los cambios de otras personas lleguen mediante un pull request aprobado por Lorenzo:

1. En GitHub, abre **Settings → Rules → Rulesets** y crea un ruleset de rama activo para `main`.
2. Añade **Repository admin** a la lista de bypass actors con permiso **Always**. En este repositorio personal, esto permite al propietario hacer push directo.
3. Activa **Require a pull request before merging**, exige al menos una aprobación y activa **Require review from Code Owners**.
4. No añadas otros usuarios, equipos o roles a la lista de bypass.

Los autores no pueden aprobar sus propios pull requests en GitHub; el propietario puede aprobar los PR creados por otras personas. La regla de bypass para administración permite al propietario seguir publicando directamente en `main`.

## Probar en local

Abre `index.html` en un navegador o sirve la carpeta con un servidor estático, por ejemplo:

```bash
python3 -m http.server 8000
```

Después visita `http://localhost:8000`.
