from django.shortcuts import render, redirect
from django.http import HttpResponse
from compras.models import CarritoCompra, CarritoCompraDetalle

def shipment_view(request):
    return render(request, 'compras/shipment.html')

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
