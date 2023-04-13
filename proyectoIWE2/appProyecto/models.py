from django.db import models

# Create your models here.

class Cliente(models.Model):
    cif = models.CharField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(max_length=20)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.cif, self.nombre, self.direccion, self.telefono, self.email

class Pedido(models.Model):
    cif = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fecha de creacion')
    cantidad = models.IntegerField(max_length=1000)
    precio = models.IntegerField(max_length=1000)

class Producto(models.Model):
    precio = models.IntegerField
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    categoria = models.CharField(max_length=200)

class Componente(models.Model):
    nombre = models.IntegerField(max_length=200)
    marca = models.IntegerField(max_length=200)

class Elemento(models.Model):
    id_producto = models.IntegerField.ForeignKey(Producto, on_delete=models.CASCADE)
    id_componente = models.IntegerField.ForeignKey(Componente, on_delete=models.CASCADE)
    cantidad = models.IntegerField(max_length=1000)