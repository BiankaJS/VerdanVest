from django.urls import path
from . import views

app_name='shopping'
urlpatterns = [
    path('shipment/', views.shipment_view, name='shipment'),
    path('cart/', views.shoppingcart_view, name='cart'),
    path('delete/<int:id>', views.deleteItemCard_view, name='deleteItemCart')
]
