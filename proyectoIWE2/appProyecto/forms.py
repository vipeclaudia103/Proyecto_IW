from django import forms
from .models import *

from django.forms.widgets import DateTimeInput


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['id_cliente', 'fecha']
        widgets = {
            'fecha': DateTimeInput(attrs={'type': 'date'})
        }

class CantidadForm(forms.ModelForm):
    class Meta:
        model = Cantidad
        fields = ['id_producto', 'n_producto']