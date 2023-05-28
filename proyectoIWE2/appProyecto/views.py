from django.forms import Form
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views import View
from django.core.paginator import Paginator
from appProyecto.forms import *
from django.urls import reverse_lazy



from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.template.loader import render_to_string


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
    context_object_name = 'productos'
    paginate_by = 3


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

            producto = formulario.save()
            url = reverse('detalle producto', args=[producto.pk])
            return redirect(url)

        return render(request, 'appProyecto/producto_create.html', {'formulario': formulario})


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'descripcion', 'categoria', ]
    template_name = "appProyecto/producto_update.html"


class PedidosListView(ListView):
    model = Pedido
    paginate_by = 3
    context_object_name = 'pedidos'


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
            pedido = formulario.save()
            url_pedido = reverse('detalle pedido', args=[pedido.pk])
            return redirect(url_pedido)
        return render(request, 'appProyecto/pedido_create.html', {'formulario': formulario})


class PedidoDetailView(DetailView):
    model = Pedido

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cantidades'] = self.object.cantidad_set.all()
        context['listaTodos'] = Pedido.objects.all()
        context['form'] = CantidadForm(
            initial={'id_pedido': self.object},
            pedido=self.object
        )
        total = 0
        for c in context['cantidades']:
            total = total + c.obtener_cantidad()
        self.object.precio = total
        self.object.save()
        context['precioTotal'] = total
        return context

    def post(self, request, *args, **kwargs):
        form = CantidadForm(request.POST)
        if form.is_valid():
            cantidad = form.save(commit=False)
            cantidad.id_pedido = self.get_object()
            cantidades = Cantidad.objects.all()
            cantidad.save()

            return redirect('detalle pedido', pk=self.get_object().pk)
        else:
            return self.get(request, *args, **kwargs)


class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = "/appProyecto/pedidos"
    template_name = "appProyecto/pedido_confirm_delete.html"


class PedidoUpdateView(UpdateView):
    model = Pedido
    fields = ['id_cliente', 'fecha']
    template_name = "appProyecto/pedido_update.html"


class ComponenteListView(ListView):
    model = Componente
    paginate_by = 4
    context_object_name = 'componentes'


class ComponenteDetailView(DetailView):
    model = Componente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['elementos'] = self.object.elemento_set.all()
        context['listaTodos'] = Componente.objects.all()
        return context


class ClientesListView(ListView):
    model = Cliente
    paginate_by = 3
    context_object_name = 'clientes'


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

            cliente = formulario.save()
            url = reverse('detalle cliente', args=[cliente.pk])
            return redirect(url)

        return render(request, 'appProyecto/cliente_create.html', {'formulario': formulario})


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = "appProyecto/cliente_update.html"


class ClienteDeleteView(DeleteView):
    model = Cliente

    success_url = "/appProyecto/clientes/"

    template_name = "appProyecto/cliente_confirm_delete.html"


class CategoriasListView(ListView):
    model = Categoria
    paginate_by = 3


class CategoriaDetailView(DetailView):
    model = Categoria

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = self.object.producto_set.all()
        context['listaTodos'] = Categoria.objects.all()
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


class CantidadUpdateView(UpdateView):
    model = Cantidad
    fields = ['n_producto']
    # success_url = "/appProyecto/pedidos/"
    template_name = "appProyecto/cantidad_update.html"


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
        if formulario.is_valid():

            componente = formulario.save()
            url = reverse('detalle componentes', args=[componente.pk])
            return redirect(url)

        return render(request, 'appProyecto/componente_create.html', {'formulario': formulario})


class ComponenteUpdateView(UpdateView):
    model = Componente
    fields = '__all__'
    template_name = "appProyecto/componente_update_form.html"


class ComponenteDeleteView(DeleteView):
    model = Componente

    success_url = "/appProyecto/componentes/"

    template_name = "appProyecto/componente_confirm_delete.html"


class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = '__all__'
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

            categoria = formulario.save()
            url = reverse('detalle categoria', args=[categoria.pk])
            return redirect(url)

        # Si los datos no son válidos, mostramos el formulario nuevamente indicando los errores
        return render(request, 'appProyecto/categoria_create.html', {'formulario': formulario})



def enviar_email(request):  
   if request.method == "POST": 
       with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           asunto = request.POST.get("asunto")  
           emisor = settings.EMAIL_HOST_USER  
           receptores = [request.POST.get("correo"), ]
           mensaje = request.POST.get("mensaje")

           context = {'asunto': asunto, 'mensaje': mensaje}
           mensaje = render_to_string('appProyecto/plantilla_email.html', context)
        
           email = EmailMessage(asunto, mensaje, emisor, receptores, connection=connection)
           email.content_subtype = 'html'
           email.send()
 
   return render(request, 'appProyecto/email.html')