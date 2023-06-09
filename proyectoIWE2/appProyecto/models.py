from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Cliente(models.Model):
    cif = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('detalle cliente', kwargs={'pk': self.pk})


class Componente(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('detalle componentes', kwargs={'pk': self.pk})


class Categoria(models.Model):
    descripcion = models.CharField(max_length=1000)
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('detalle categoria', kwargs={'pk': self.pk})


class Producto(models.Model):
    precio = models.FloatField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
     )
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    componente = models.ManyToManyField(Componente, through="Elemento")

    def obtener_precio(self):
        return self.precio

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('detalle producto', kwargs={'pk': self.pk})


class Elemento(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    cantidad = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ]
     )

    class Meta:
        unique_together = (('id_producto', 'id_componente'),)


class Pedido(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fecha de creacion')
    precio = models.FloatField(default=0)
    producto = models.ManyToManyField(Producto, through="Cantidad")

    def __str__(self):
        return f"{self.id_cliente} - {self.fecha}"
    
    def get_absolute_url(self):
        return reverse('detalle pedido', kwargs={'pk': self.pk})


class Cantidad(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    n_producto = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ]
     )

    def obtener_cantidad(self):
        return self.n_producto * self.id_producto.obtener_precio()

    class Meta:
        unique_together = (('id_producto', 'id_pedido'),)

    def get_absolute_url(self):
        return reverse('detalle pedido', kwargs={'pk': self.id_pedido.pk})