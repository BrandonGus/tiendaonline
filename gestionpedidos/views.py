from django.shortcuts import render
from django.http import HttpResponse

def busqueda_productos(request):
    return render(request, "busqueda.html")

def buscar(request):
    mensaje="articulo buscado: %r" %request.GET["productos"]
    return HttpResponse(mensaje)