from django.db import models

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=355)
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="posts")

    def __str__(self) -> str:
        return self.titulo
