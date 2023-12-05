from django.shortcuts import render, redirect
from django.http import HttpResponse
from compras.models import CarritoCompra, CarritoCompraDetalle, Pago, Pedido, PedidoDetalle
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal

@login_required
def shipment_view(request):
    if(request.user):
        cart = CarritoCompra.objects.get(usuario_id=request.user.id)
        detail_cart = CarritoCompraDetalle.objects.filter(carrito_compra=cart)
        total_cart = sum(detalle.producto.precio * detalle.cantidad for detalle in detail_cart)
        context = {
            'domicilio': request.user.domicilio,
            'detail_cart': detail_cart,
            'total_cart': total_cart
        }
    return render(request, 'compras/shipment.html', context)

def shoppingcart_view(request):
    if(request.user):
        try: 
            cart = CarritoCompra.objects.get(usuario_id=request.user.id)
            detail_cart = CarritoCompraDetalle.objects.filter(carrito_compra=cart)
            total_cart = sum(detalle.producto.precio * detalle.cantidad for detalle in detail_cart)
            context = {
                'cart': cart,
                'detail_cart': detail_cart,
                'total_cart': total_cart
            }
        except: 
            context = {
            }

        return render(request, 'compras/shoppingcart.html', context)
    else:
        return redirect('auth:login')

def deleteItemCard_view(request, id):
    product = get_object_or_404(CarritoCompraDetalle, pk=id)
    product.delete()
    return redirect('shopping:cart')

def savePayCart_view(request):
    if(request.method == "POST"):
        if(request.user):
            cart = CarritoCompra.objects.get(usuario_id=request.user.id)
            detail_cart = CarritoCompraDetalle.objects.filter(carrito_compra=cart)
            total_cart = sum(detalle.producto.precio * detalle.cantidad for detalle in detail_cart)
            pay = Pago.objects.create(usuario=request.user, cantidad = 10000.00, folio='AOIAIDOO', metodo_pago=1, fecha_pago=timezone.now(), descripcion='', estado_pago='COMPLETO', numero_referencia='11111', informacion_pago='kjklsdfjd')
            pay.save()
            fecha = timezone.now() + timedelta(days=2)
            pedido = Pedido.objects.create(direccion_envio=request.user.domicilio, usuario=request.user, fecha_entrega_estimada=fecha, total=total_cart)
            pedido.save()
            for detalle in detail_cart:
                decimal = Decimal(detalle.cantidad)
                pedidoDetalle = PedidoDetalle.objects.create(pedidoId=pedido, cantidad=decimal, producto=detalle.producto)
                pedidoDetalle.save()

            cart.delete()
            return redirect('auth:profile')