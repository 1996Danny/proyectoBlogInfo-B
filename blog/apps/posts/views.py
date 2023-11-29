# import get_objetc
from django.shortcuts import render, get_object_or_404

# importar la clase Post del models (BD)
from .models import Post


# Create your views here.
def home_post(request):
    return render(request, "home.html")


def post(request):
    return render(request, "post.html")


def post_realizado(request):
    posteos = Post.objects.all()  # selec * from Post
    return render(request, "posts/post.html", {"posteos": posteos})


def post_detail(request, post_id):
    # traer el post con id y si no encuentra error 404
    post = get_object_or_404(Post, pk=post_id)
    ctx = {"post": post}
    return render(request, "posts/post_detail.html", ctx)


# def categorias_post(request):
#     return render(request, "posts/categorias.html")
