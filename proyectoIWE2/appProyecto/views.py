from django.forms import Form
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views import View
from appProyecto.forms import *
from django.urls import reverse_lazy


def inicio(request):
    return render(request, 'inicio.html')


class ElementoDeleteView(DeleteView):
    model = Elemento
    success_url = "/appProyecto/productos"

    def get_success_url(self):
        return reverse_lazy('detalle producto', kwargs={'pk': self.object.id_producto.pk})


class CantidadDeleteView(DeleteView):
    model = Cantidad
    success_url = "/appProyecto/pedidos"

    def get_success_url(self):
        return reverse_lazy('detalle pedido', kwargs={'pk': self.object.id_pedido.pk})


class ProductosListView(ListView):
    model = Producto
    context_object_name = 'producto'


class ProductoDetailView(DetailView):
    model = Producto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['elementos'] = self.object.elemento_set.all()
        context['form'] = ElementoForm(initial={'id_producto': self.object})
        context['listaTodos'] = Producto.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = ElementoForm(request.POST)
        if form.is_valid():
            elemento = form.save(commit=False)
            elemento.id_producto = self.get_object()
            elemento.save()
            return redirect('detalle producto', pk=self.get_object().pk)
        else:
            return self.get(request, *args, **kwargs)


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = "/appProyecto/productos"
    template_name = "appProyecto/produto_confirm_delete.html"


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


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'descripcion', 'categoria', ]
    success_url = "/appProyecto/productos"
    template_name = "appProyecto/producto_update.html"


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cantidades'] = self.object.cantidad_set.all()
        context['listaTodos'] = Pedido.objects.all()
        total = 0
        for c in context['cantidades']:
            total = total + c.obtener_cantidad()
        context['precioTotal'] = total
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedidos'] = self.object.pedido_set.all()
        context['listaTodos'] = Cliente.objects.all()
        return context


class ClienteCreateView(View):
    def get(self, request, *args, **kwargs):
        formulario = ClienteForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appProyecto/cliente_create.html', context)

    def post(self, request, *args, **kwargs):
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista clientes')
        return render(request, 'appProyecto/cliente_create.html', {'formulario': formulario})


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = "/appProyecto/clientes"
    template_name = "appProyecto/cliente_update.html"


class ClienteDeleteView(DeleteView):
    model = Cliente

    success_url = "/appProyecto/clientes/"

    template_name = "appProyecto/cliente_confirm_delete.html"


class CategoriasListView(ListView):
    model = Categoria


class CategoriaDetailView(DetailView):
    model = Categoria

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = self.object.producto_set.all()
        return context


class CantidadCreateView(View):
    def get(self, request, *args, **kwargs):
        formulario = CantidadForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appProyecto/cantidad_create.html', context)

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
    success_url = "/appProyecto/componentes/"
    template_name = "appProyecto/componente_update_form.html"


class ComponenteDeleteView(DeleteView):
    model = Componente

    success_url = "/appProyecto/componentes/"

    template_name = "appProyecto/componente_confirm_delete.html"


class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = '__all__'
    success_url = "/appProyecto/categoria/"
    template_name = "appProyecto/categoria_update_form.html"


class CategoriaDeleteView(DeleteView):
    model = Categoria

    success_url = "/appProyecto/categoria/"

    template_name = "appProyecto/categoria_confirm_delete.html"


class CategoriaCreateView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        formulario = CategoriaForm()
        context = {
            'formulario': formulario
        }
        return render(request, 'appProyecto/categoria_create.html', {'formulario': formulario})

    def post(self, request, *args, **kwargs):
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():  # is_valid() deja los datos validados en el atributo cleaned_data
            formulario.save()

            # Volvemos a la lista de departamentos
            return redirect('lista categorias')
        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'appProyecto/categoria_create.html', {'formulario': formulario})
