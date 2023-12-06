# import get_objetc
from django.shortcuts import render, get_object_or_404, redirect

# importar la clase Post del models (BD)
from .models import Post, Categoria, Comentario


# Create your views here.
def home_post(request):
    return render(request, "home.html")


def post(request):
    return render(request, "post.html")


def post_realizado(request):
    # posteos = Post.objects.all()  # selec * from Post
    # categorias = Categoria.objects.all()
    # print(categorias)
    # print(posteos)
    id_categoria = request.GET.get("id", None)
    if id_categoria:
        posteos = Post.objects.filter(categoria_post=id_categoria)
    else:
        posteos = Post.objects.all()  # una lista

    categorias = Categoria.objects.all()
    ctx = zip(posteos, categorias)

    return render(request, "posts/post.html", {"ctx": ctx, "posteos": posteos})


def post_detail(request, post_id):
    # traer el post con id y si no encuentra error 404
    post = get_object_or_404(Post, pk=post_id)
    ctx = {"post": post}
    return render(request, "posts/post_detail.html", ctx)


# def categorias_post(request):
#     return render(request, "posts/categorias.html")


def comentar_posteo(request):
    comentario = request.POST.get("comentario", None)
    usuario = request.user
    post = request.POST.get("id_post", None)
    posteo = Post.objects.get(id=post)
    setear_comentario = Comentario.objects.create(
        usuario=usuario, post=posteo, texto=comentario
    )
    return redirect("posts:post_detail", post_id=post)
