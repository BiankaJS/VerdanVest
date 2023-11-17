from django.db import models
from catalogo.models import Producto
from django.conf import settings

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    serie = models.TextField(null=True, blank=True)
    folio = models.TextField(null=True, blank=True)
    direccion_envio = models.TextField(null=True, blank=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    numero_seguimiento = models.CharField(max_length=50, null=True, blank=True)
    fecha_entrega_estimada = models.DateTimeField(null=True, blank=True)

class PedidoDetalle(models.Model):
    pedidoId = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    folio = models.TextField()
    metodo_pago = models.PositiveIntegerField()
    fecha_pago = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)
    estado_pago = models.CharField(max_length=20, default='PENDIENTE')
    numero_referencia = models.CharField(max_length=50, blank=True, null=True)
    informacion_pago = models.TextField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class CarritoCompra(models.Model):
    id = models.AutoField(primary_key=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class CarritoCompraDetalle(models.Model):
    carrito_compra = models.ForeignKey(CarritoCompra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
