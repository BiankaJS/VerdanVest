from django.shortcuts import render
from django.http import HttpResponse

def shipment_view(request):
    return render(request, 'compras/shipment.html')

def shoppingcart_view(request):
    return render(request, 'compras/shoppingcart.html')
