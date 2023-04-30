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
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = ['id_componente', 'cantidad']