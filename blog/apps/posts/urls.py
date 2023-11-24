from django.urls import path

# Import views
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.home_post, name="home_posts"),
    path("categorias", views.categorias_post, name="categorias_posts"),
]
