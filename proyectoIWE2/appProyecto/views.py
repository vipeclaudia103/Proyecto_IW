from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def inicio(request):
    return render(request, 'inicio.html')


def producto(request):
    productos = Producto.objects.order_by('nombre')
    context = {'lista_productos': productos}
    return render(request, 'producto.html', context)
