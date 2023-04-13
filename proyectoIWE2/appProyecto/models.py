from django.db import models

# Create your models here.


class Cliente(models.Model):
    cif = models.CharField(primary_key=True, max_length=100)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(default=0)
    email = models.EmailField(max_length=200)


class Componente(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)


class Producto(models.Model):
    precio = models.IntegerField
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    categoria = models.CharField(max_length=200)
    componentes = models.ManyToManyField(Componente, through="Elemento")


class Elemento(models.Model):
    id_producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE)
    id_componente = models.ForeignKey(
        Componente, on_delete=models.CASCADE)
    # index = models.
    cantidad = models.IntegerField(default=0)


class Pedido(models.Model):
    cif = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_producto = models.ManyToManyField(Producto)
    fecha = models.DateTimeField('Fecha de creacion')
    cantidad = models.IntegerField(default=0)
    precio = models.FloatField(default=0)


# host = models.ForeignKey(User, related_name='host_set')
