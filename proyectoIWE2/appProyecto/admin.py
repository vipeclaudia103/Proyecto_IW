from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Componente)
admin.site.register(Elemento)

