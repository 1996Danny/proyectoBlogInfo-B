from django.http import HttpResponse

# render
from django.shortcuts import render


def despedida(request):
    return HttpResponse("Buenas Noches!")


def saludo(request):
    return render(request, "index.html")


def nombre(request):
    return HttpResponse("Daniel" + " Frias")
