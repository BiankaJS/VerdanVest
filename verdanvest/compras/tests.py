from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import CarritoCompra, CarritoCompraDetalle, Producto

class ComprasViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def create_test_product(self):
        # Crear un producto de prueba
        return Producto.objects.create(nombre='Test Product', precio=10.0)

    def create_test_cart_and_detail(self):
        # Crear un carrito de compra de prueba y un detalle asociado
        cart = CarritoCompra.objects.create(usuario=self.user)
        product = self.create_test_product()
        detail_cart = CarritoCompraDetalle.objects.create(carrito_compra=cart, producto=product, cantidad=2)
        return cart, detail_cart

    def test_shipment_view(self):
        # Prueba para la vista 'compras:shipment_view'
        response = self.client.get(reverse('compras:shipment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'compras/shipment.html')

    def test_shoppingcart_view_authenticated_user(self):
        # Prueba para la vista 'compras:shoppingcart_view' con un usuario autenticado
        cart, detail_cart = self.create_test_cart_and_detail()
        response = self.client.get(reverse('compras:shoppingcart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'compras/shoppingcart.html')
        self.assertEqual(response.context['cart'], cart)
        self.assertEqual(response.context['detail_cart'].count(), 1)
        self.assertEqual(response.context['total_cart'], 20.0)

    def test_shoppingcart_view_unauthenticated_user(self):
        # Prueba para la vista 'compras:shoppingcart_view' con un usuario no autenticado
        self.client.logout()
        response = self.client.get(reverse('compras:shoppingcart'))
        self.assertEqual(response.status_code, 302)  # Redirección a la página de inicio de sesión
        self.assertRedirects(response, reverse('auth:login'))

    def test_deleteItemCard_view(self):
        # Prueba para la vista 'compras:deleteItemCard_view'
        cart, detail_cart = self.create_test_cart_and_detail()
        response = self.client.get(reverse('compras:deleteItemCard', args=[detail_cart.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('compras:shoppingcart'))

        # Verificar que el detalle del carrito haya sido eliminado
        self.assertEqual(CarritoCompraDetalle.objects.count(), 0)