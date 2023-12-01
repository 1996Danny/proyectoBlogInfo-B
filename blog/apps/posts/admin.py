from django.contrib import admin

# Register your models here.
from .models import Post, Categoria

# resgistamos la clase para ver en el panel de administrador
admin.site.register(Post)
admin.site.register(Categoria)
