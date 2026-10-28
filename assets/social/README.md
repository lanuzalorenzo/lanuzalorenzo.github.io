# Piezas de redes

Portada y avatar con la marca LL. La geometría de la marca está en [`assets/marca/README.md`](../marca/README.md).

## Portada de LinkedIn

`linkedin-cover.svg` es la fuente y `linkedin-cover.png` la versión a 1584×396. Lleva solo la marca en el centro de las tres órbitas del sitio, sin texto: el perfil ya muestra nombre y puesto justo debajo, y en móvil la portada se ve a unos 375 px de ancho, donde cualquier rótulo quedaría por debajo de los 5 px. La marca va centrada en la mitad derecha para no chocar con la foto de perfil, que en escritorio ocupa la esquina inferior izquierda.

`linkedin-cover-preview.png` es una vista de comprobación, no se publica: escritorio arriba y móvil abajo.

## Avatar

`avatar-400.png` es la pieza para GitHub y LinkedIn, 400×400 y recortada en primer plano.

Es foto, no marca, y es una decisión explícita: en LinkedIn y GitHub el avatar identifica a una persona, y a 32 px una cara se lee como alguien mientras que un símbolo se lee como una empresa. La marca no se pierde: sigue en el favicon, en los iconos y en la portada.

Pendiente de mejorar: el fondo de la foto lleva nube, circuitos y HUD, que es un cliché y no usa el azul de la marca. A 32 px se convierte en textura, pero a 128 se nota. Lo que lo arregla es una foto nueva con fondo `#07131e` liso y luz de borde cian, no un filtro.

El fondo ocupa el cuadrado completo y no lleva borde: GitHub y LinkedIn recortan el avatar en círculo y un borde en el canto se perdería. La cara se queda dentro del círculo inscrito.
