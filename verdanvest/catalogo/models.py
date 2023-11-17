from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    ventas_totales = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    unidades_vendidas = models.PositiveIntegerField(default=0)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField(null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    calificacion_salud = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True) 
    urlImagen = models.TextField(null=True, blank=True)

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

