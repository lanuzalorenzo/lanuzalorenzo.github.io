<img src="assets/iconos/web.svg" width="64" alt="Icono de la web personal">

# Web personal — Lorenzo Lanuza

Sitio estático de presentación profesional, experiencia, especialidades y proyectos. Comicteca aparece como aplicación principal; el banco de pruebas, el laboratorio asíncrono de eventos y el laboratorio de IA aplicada se presentan como proyectos destacados, no como tema principal. Los diagramas de cada proyecto son SVG en línea, sin dependencias externas.

## Contenido

- **Perfil:** presentación, especialidades, formación y certificaciones.
- **Experiencia:** trayectoria profesional.
- **Proyectos:** Comicteca como aplicación principal, el Portfolio de seguridad con `EcommerceApi` como banco de pruebas, `eventos-api` como laboratorio asíncrono, e IA aplicada.
- **Comicteca:** la aplicación principal, con el estado real de 27 controles y límites —aplicación, controles compartidos, identidad y datos, CI y alcance declarado— y enlace a su prueba.
- **Portfolio de seguridad:** doce módulos y un laboratorio final con [evidencias indexadas](https://github.com/lanuzalorenzo/portfolio-ciberseguridad-lorenzo/blob/main/laboratorio-final/evidencias/README.md) por tipo y fecha.
- **IA aplicada:** guías y experimentos de IA local con Ollama, con criterio y límites.
- **El banco de pruebas (`EcommerceApi`):** el estado real de 28 controles y límites, con enlace a la evidencia de cada uno.
- **El laboratorio asíncrono (`eventos-api`):** el estado real de 16 controles —seguridad de aplicación y entrega y repositorio—, con enlace a su evidencia.
- **Contacto y CV:** enlaces profesionales y PDF optimizado para ATS.

## Estructura

La cabecera y el pie viven en `identidad/plantilla.tpl`; la nav canónica, en `identidad/shell.py`; el contenido de cada página, en `src/pages/`. Los seis HTML de la raíz son artefactos generados: no se editan a mano.

```bash
python3 scripts/build.py          # regenera index.html, portfolio.html, comicteca.html, api.html, eventos.html e ia.html
python3 scripts/build.py --check  # falla si lo versionado no coincide con lo generado
```

## Publicar en GitHub Pages

Las cabeceras HTTP las fija GitHub Pages, no este repositorio: no se presentan como control propio ni se comprueba aquí la cabecera `Server`.

1. Crea un repositorio público llamado exactamente `lanuzalorenzo.github.io` en la cuenta `lanuzalorenzo`.
2. Desde esta carpeta, publica los archivos en la rama `main`:

   ```bash
   git add .
   git commit -m "feat(site): create personal portfolio website"
   git push -u origin main
   ```

3. En GitHub, abre **Settings → Pages** y selecciona **GitHub Actions** como origen de publicación.
4. El workflow de `.github/workflows/pages.yml` desplegará el sitio. La dirección será `https://lanuzalorenzo.github.io/`.

Cada `push` a `main` volverá a publicar la web. El workflow copia a `_site` solo los archivos públicos del sitio (`index.html`, `portfolio.html`, `comicteca.html`, `api.html`, `eventos.html`, `ia.html`, `styles.css`, `app.js`, `assets`, favicons, `.nojekyll`, `robots.txt` y `sitemap.xml`), de modo que las fuentes de las páginas (`src/`), la documentación interna y el historial de Git no forman parte del artefacto. Al cambiar el contenido, actualiza `lastmod` en `sitemap.xml`.

El botón **Descargar CV** entrega el PDF real alojado en `assets/cv/lanuza-lorenzo-cv.pdf` (CV de 2 páginas optimizado para ATS), no una copia impresa de la página. Para actualizarlo, reemplaza ese fichero manteniendo el mismo nombre: la URL no cambia y los enlaces ya compartidos siguen funcionando.

## Protección de la rama `main`

`.github/CODEOWNERS` asigna la revisión del código a `@lanuzalorenzo`. La protección se aplica con un ruleset de rama activo para `main`:

- Pull request obligatorio.
- Cero aprobaciones obligatorias: el repositorio tiene un solo mantenedor y GitHub no permite aprobar el propio PR.
- Check `Verificación (secretos y enlaces)` en verde.
- Rama actualizada antes del merge.
- Squash como único método de merge.
- Force push y borrado de `main` bloqueados.
- Sin bypass actors: solo el propietario tiene permiso de escritura y merge, salvo el flujo automático de Dependabot para parches y minors con los checks en verde.

Los cambios de otras personas llegan por pull request y los fusiona el propietario. El propietario no publica directamente en `main`. La excepción es Dependabot: sus PRs de parche y minor las fusiona el flujo automático si pasan los checks.

## Licencia

El código —`scripts/`, `src/`, `styles.css`, `app.js` y los HTML generados— va con **MIT** ([`LICENSE`](LICENSE)). Los textos, las fotografías, el CV y el monograma LL van con **CC BY-ND 4.0** ([`LICENSE-CONTENT`](LICENSE-CONTENT)): se pueden citar y compartir sin modificarlos y con atribución.

## Probar en local

Sirve la carpeta con un servidor estático, por ejemplo:

```bash
python3 -m http.server 8000
```

Después visita `http://localhost:8000`. Abrir `index.html` con `file://` no sirve: la marca y los enlaces al inicio usan la raíz `/`.
