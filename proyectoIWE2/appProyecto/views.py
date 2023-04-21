from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, get_list_or_404


def inicio(request):
    return render(request, 'inicio.html')


class ProductosListView(ListView):
    model = Producto
    context_object_name = 'producto'


class ProductoDetailView(DetailView):
    model = Producto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['elementos'] = self.object.elemento_set.all()
        return context


class PedidosListView(ListView):
    model = Pedido


class PedidoDetailView(DetailView):
    model = Pedido


class ComponentesListView(ListView):
    model = Componente


class ComponenteDetailView(DetailView):
    model = Componente


class ClientesListView(ListView):
    model = Cliente


class ClienteDetailView(DetailView):
    model = Cliente


class CategoriasListView(ListView):
    model = Categoria


class CategoriaDetailView(DetailView):
    model = Categoria


# def producto(request):
#     Pedido = Producto.objects.order_by('nombre')
#     context = {'lista_productos': productos}
#     return render(request, 'producto.html', context)
