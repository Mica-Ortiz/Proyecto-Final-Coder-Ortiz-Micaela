from django.contrib import admin

from .models import *

admin.site.register(Usuario)
admin.site.register(Recetas)
admin.site.register(Categoría)
admin.site.register(Comentarios)