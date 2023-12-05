from django.test import TestCase, Client
from django.urls import reverse
from .models import Contacto

# Create your tests here.
class HomeViewTestCase(TestCase):

    def setUp(self):
        # Configuración inicial, si es necesario
        self.client = Client()

    def test_home_view_get(self):
        # Prueba para una solicitud GET a la vista 'home'
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_home_view_post(self):
        # Prueba para una solicitud POST a la vista 'home'
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '123456789',
            'message': 'Test message'
        }

        response = self.client.post(reverse('home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

        # Verificar que se haya guardado el objeto Contacto en la base de datos
        self.assertEqual(Contacto.objects.count(), 1)

        # Obtener el objeto Contacto creado y verificar sus atributos
        contacto = Contacto.objects.first()
        self.assertEqual(contacto.nombre, 'John Doe')
        self.assertEqual(contacto.email, 'john@example.com')
        self.assertEqual(contacto.telefono, '123456789')
        self.assertEqual(contacto.mensaje, 'Test message')

    def test_home_view_exception(self):
        # Prueba para la vista 'home' cuando ocurre una excepción
        with self.assertRaises(Exception):
            # Forzamos una excepción al hacer una solicitud POST sin datos
            self.client.post(reverse('home'))

        # Verificar que la vista renderice 'contact.html'
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')