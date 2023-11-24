from django.http import HttpResponse

# render
from django.shortcuts import render


def contacto(request):
    return render(request, "contacto.html")


def acerca_de(request):
    return render(request, "acerca_de.html")


# def despedida(request):
#     return HttpResponse("Buenas Noches!")


# def saludo(request):
#     return render(request, "index.html")


# def nombre(request):
#     return HttpResponse("Daniel" + " Frias")
