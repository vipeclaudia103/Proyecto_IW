from django.forms import Form
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views import View
from appProyecto.forms import *


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


class ProductoCreateView(View):
    def get(self, request, *args, **kwargs):
        formulario = ProductoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appProyecto/producto_create.html', context)

    def post(self, request, *args, **kwargs):
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():

            formulario.save()

            return redirect('lista productos')
        return render(request, 'appProyecto/producto_create.html', {'formulario': formulario})


class PedidosListView(ListView):
    model = Pedido


class PedidoCreateView(View):
    def get(self, request, *args, **kwargs):
        formulario = PedidoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appProyecto/pedido_create.html', context)

    def post(self, request, *args, **kwargs):
        formulario = PedidoForm(request.POST)
        if formulario.is_valid():

            formulario.save()

            return redirect('lista pedidos')
        return render(request, 'appProyecto/pedido_create.html', {'formulario': formulario})


class PedidoDetailView(DetailView):
    model = Pedido


class ComponenteListView(ListView):
    model = Componente


class ComponenteDetailView(DetailView):
    model = Componente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['elementos'] = self.object.elemento_set.all()
        return context


class ClientesListView(ListView):
    model = Cliente


class ClienteDetailView(DetailView):
    model = Cliente


class ClienteCreateView(View):
    def get(self, request, *args, **kwargs):
        formulario = ClienteForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appProyecto/pedido_list.html', context)

    def post(self, request, *args, **kwargs):
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista pedidos')
        return render(request, 'appProyecto/pedido_list.html', {'formulario': formulario})


class CategoriasListView(ListView):
    model = Categoria


class CategoriaDetailView(DetailView):
    model = Categoria


class CantidadCreateView(View):
    def get(self, request, *args, **kwargs):
        formulario = CantidadForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appProyecto/pedido_list.html', context)

    def post(self, request, *args, **kwargs):
        formulario = CantidadForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            return redirect('lista pedidos')
        return render(request, 'appProyecto/pedido_list.html', {'formulario': formulario})


class ComponenteCreateView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        formulario = ComponenteForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appProyecto/componente_create.html', {'formulario': formulario})

    def post(self, request, *args, **kwargs):
        formulario = ComponenteForm(request.POST)
        if formulario.is_valid():  # is_valid() deja los datos validados en el atributo cleaned_data
            formulario.save()

            # Volvemos a la lista de departamentos
            return redirect('lista componentes')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'appProyecto/componente_create.html', {'formulario': formulario})


class ComponenteUpdateView(UpdateView):
    model = Componente
    fields = '__all__'
    success_url = "/appProyecto/componentes"
    template_name = "appProyecto/componente_update_form.html"


class ComponenteDeleteView(DeleteView):
    model = Componente

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/appProyecto/componentes"

    template_name = "appProyecto/componente_confirm_delete.html"
