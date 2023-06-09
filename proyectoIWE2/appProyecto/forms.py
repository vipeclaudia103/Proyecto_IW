from django import forms
from .models import *

from django.forms.widgets import DateTimeInput


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'categoria', ]


class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'


class PedidoForm(forms.ModelForm):
    fecha = forms.DateField(
        label='Fecha', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Pedido
        fields = ['id_cliente', 'fecha']
        # widgets = {
        #     'fecha': DateTimeInput(attrs={'type': 'date'})
        # }


class CantidadForm(forms.ModelForm):
    class Meta:
        model = Cantidad
        fields = ['id_producto', 'n_producto',]

    def __init__(self, *args, **kwargs):
        pedido = kwargs.pop('pedido', None)
        super().__init__(*args, **kwargs)
        if pedido:
            productos_en_pedido = pedido.producto.all()
            self.fields['id_producto'].queryset = Producto.objects.exclude(
                id__in=productos_en_pedido
            )


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = ['id_componente', 'cantidad']
    
    def __init__(self, *args, **kwargs):
        producto = kwargs.pop('producto', None)
        super().__init__(*args, **kwargs)
        if producto:
            componenetes_en_producto = producto.componente.all()
            self.fields['id_pedido'].queryset = Componente.objects.exclude(
                id__in=componenetes_en_producto
            )

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'