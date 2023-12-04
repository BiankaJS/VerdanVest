from django.db import models
from ingredientes_materiales.models import Material, Ingrediente

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField(null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default=1)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default= 1)
    calificacion_salud = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True) 
    urlImagen = models.TextField(null=True, blank=True)

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class ProductoMaterial(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

class ProductoIngrediente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)