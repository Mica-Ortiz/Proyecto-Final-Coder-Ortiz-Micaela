# Proyecto_PR

Página web de recetas de cocina. 

Tiene pocas funcionalidades desarrolladas por el momento. La idea es que las personas puedan registrarse creando un usuario, subir
recetas, comentarlas y buscar recetas.

Clases (por el momento):
 - Recetas
 - Categorías
 - Usuarios
 - Comentarios

Se crearon las vistas: index, recetas, categorias, comentarios.

Se creó el archivo base.html. El archivo index.html hereda de él. 

Las otras vistas no se terminaron. La idea es que también herenden del base.html.

Por el momento se puede navegar entre los templates: index.html y recetas.html con los botones Inicio y Recetas en la parte superior derecha de la página.

Se crearon formularios para las clases: Recetas, Categorías, Usuario.

Para insertar datos en la BD mediante formularios hay que dirigirse a las siguientes urls:
- 'servidor'/AppRecetas/formulario_receta
- 'servidor'/AppRecetas/formulario_categoria
- 'servidor'/AppRecetas/formulario_usuario

Para buscar datos en la BD mediante formularios hay que dirigirse a las siguientes urls:
- 'servidor'/AppRecetas/busqueda_receta
- 'servidor'/AppRecetas/busqueda_categoria
- 'servidor'/AppRecetas/busqueda_usuario

Para ingresar al admin:
- usser: Micaela
- password: MIMOSHI345
