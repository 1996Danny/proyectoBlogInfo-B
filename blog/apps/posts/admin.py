from django.contrib import admin

# Register your models here.
from .models import Post

# resgistamos la clase para ver en el panel de administrador
admin.site.register(Post)
