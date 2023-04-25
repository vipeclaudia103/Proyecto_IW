from django.shortcuts import get_object_or_404, render, redirect
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
        formulario = ProductoForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appProyecto/pedido_create.html', context)
     
     def post(self, request, *args, **kwargs):
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():

            formulario.save()

            return redirect('lista pedidos')
        return render(request, 'appProyecto/pedido_create.html', {'formulario': formulario})

class PedidoDetailView(DetailView):
    model = Pedido

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pedido = get_object_or_404(Pedido, pk=self.kwargs['pk'])
        context['cantidad'] = pedido.cantidad_set.all()
        return context


class ComponenteListView(ListView):
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
