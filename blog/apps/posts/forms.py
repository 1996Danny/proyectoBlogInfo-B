from django import forms

from .models import Comentario, Post


class Formulario_Modificacion(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("texto",)


class Form_Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "titulo",
            "cuerpo",
            "imagen",
            "categoria_post",
        )
