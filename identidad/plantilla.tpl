<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="dark">
    <meta name="theme-color" content="#07131e">
    <meta name="description" content="{{descripcion}}">
    <title>{{titulo}}</title>
<!-- perfil:publica -->
<!-- si:canonical -->
    <link rel="canonical" href="{{canonical}}">
<!-- /si:canonical -->
{{og_meta}}
<!-- /perfil:publica -->
<!-- perfil:local -->
    <meta name="robots" content="noindex, nofollow">
<!-- /perfil:local -->
{{head_extra}}
{{estilos}}
  </head>
  <body{{atributos_cuerpo}}>
    <a class="skip-link" href="#contenido">Saltar al contenido</a>
{{antes_cabecera}}
    <header class="site-header">
      <a class="wordmark" href="{{inicio}}" aria-label="Lorenzo Lanuza, inicio"><img src="{{marca_svg}}" alt="" width="40" height="40"></a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
        <span class="sr-only">Abrir menú</span>
        <span class="menu-line menu-line-top"></span><span class="menu-line menu-line-bottom"></span>
      </button>
      <nav class="site-nav" id="site-nav" aria-label="Navegación principal">
{{nav}}
      </nav>
    </header>

{{cuerpo}}

    <footer class="site-footer">
      <a class="wordmark" href="{{inicio}}" aria-label="Lorenzo Lanuza, inicio"><img src="{{marca_svg}}" alt="" width="40" height="40"></a>
<!-- si:repo -->
      <a href="{{repo}}" target="_blank" rel="noreferrer">Código en GitHub <span aria-hidden="true">↗</span></a>
<!-- /si:repo -->
      <a href="{{arriba}}">Volver arriba <span aria-hidden="true">↑</span></a>
      <span>{{pie_nota}}</span>
    </footer>
<!-- si:menu_js -->
    <script src="{{menu_js}}" defer></script>
<!-- /si:menu_js -->
{{scripts}}
  </body>
</html>
