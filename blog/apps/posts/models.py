from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=355)
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="posts")
    categoria_post = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def comentarios_realizados(self):
        return self.comentario_set.all()

    def __str__(self) -> str:
        return self.titulo


class Comentario(models.Model):
    texto = models.TextField(max_length=1000)
    fecha_comentacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.post} {self.texto}"
