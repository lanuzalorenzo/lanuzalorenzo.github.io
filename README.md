# Web personal — Lorenzo Lanuza

Sitio estático de presentación profesional, experiencia, especialidades y proyectos. El laboratorio de seguridad —portfolio y su API— está enlazado como proyecto destacado, no como tema principal.

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

Cada `push` a `main` volverá a publicar la web. El botón **Descargar CV** entrega el PDF real alojado en `assets/cv/lanuza-lorenzo-cv.pdf` (CV de 2 páginas optimizado para ATS), no una copia impresa de la página. Para actualizarlo, reemplaza ese fichero manteniendo el mismo nombre: la URL no cambia y los enlaces ya compartidos siguen funcionando.

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
