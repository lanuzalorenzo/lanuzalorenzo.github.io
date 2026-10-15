# Web personal — Lorenzo Lanuza

Sitio estático de presentación profesional, experiencia, especialidades y proyectos. El portfolio de ciberseguridad está enlazado como proyecto destacado, no como tema principal.

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

Cada `push` a `main` volverá a publicar la web. El botón **Imprimir / guardar CV** abre el diálogo del navegador para imprimir la página o guardarla como PDF.

## Probar en local

Abre `index.html` en un navegador o sirve la carpeta con un servidor estático, por ejemplo:

```bash
python3 -m http.server 8000
```

Después visita `http://localhost:8000`.
