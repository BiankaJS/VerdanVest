from django.urls import path
from . import views

urlpatterns = [
    path('shipment/', views.shipment_view, name='shipment'),
    path('shoppingcart/', views.shoppingcart_view, name='shoppingcart')
]
