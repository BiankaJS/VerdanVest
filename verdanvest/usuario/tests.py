from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .models import Pedido, PedidoDetalle

class AuthViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_login_view_valid_credentials(self):
        # Crear un usuario de prueba
        User.objects.create_user(username='testuser', password='testpassword')

        # Realizar una solicitud POST con credenciales válidas
        response = self.client.post(reverse('auth:login'), {'username': 'testuser', 'password': 'testpassword'})
        
        # Verificar que la respuesta sea una redirección a 'home:Home'
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:Home'))

    def test_login_view_invalid_credentials(self):
        # Realizar una solicitud POST con credenciales inválidas
        response = self.client.post(reverse('auth:login'), {'username': 'invaliduser', 'password': 'invalidpassword'})
        
        # Verificar que la respuesta es una renderización de 'usuario/login.html' con un mensaje de error
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuario/login.html')
        self.assertContains(response, "Invalid email or password. Please try again.")

    def test_register_view_success(self):
        # Realizar una solicitud POST con datos válidos
        response = self.client.post(reverse('auth:register'), {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        })

        # Verificar que la respuesta sea una redirección a 'auth:login'
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('auth:login'))

        # Verificar que se haya creado un nuevo usuario
        self.assertEqual(User.objects.filter(username='newuser').count(), 1)

    def test_profile_view_authenticated_user(self):
        # Iniciar sesión como usuario de prueba
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(test_user)

        # Realizar una solicitud GET a la vista 'auth:profile'
        response = self.client.get(reverse('auth:profile'))

        # Verificar que la respuesta sea un código 200 y la renderización de 'usuario/profile.html'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuario/profile.html')

        # Verificar que se pasan los datos correctos al contexto
        self.assertEqual(response.context['user'], test_user)

    def test_profile_view_unauthenticated_user(self):
        # Realizar una solicitud GET a la vista 'auth:profile' sin iniciar sesión
        response = self.client.get(reverse('auth:profile'))

        # Verificar que la respuesta sea una redirección a 'auth:login'
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('auth:login'))

    def test_logout_view(self):
        # Iniciar sesión como usuario de prueba
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(test_user)

        # Realizar una solicitud GET a la vista 'auth:logout'
        response = self.client.get(reverse('auth:logout'))

        # Verificar que la respuesta sea una redirección a 'home:Home'
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:Home'))

    def test_addAddress_view(self):
        # Iniciar sesión como usuario de prueba
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(test_user)

        # Realizar una solicitud POST a la vista 'auth:addAddress_view' con una dirección
        response = self.client.post(reverse('auth:addAddress_view'), {'address': '123 Main St'})

        # Verificar que la respuesta sea una redirección a 'auth:profile'
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('auth:profile'))

        # Obtener el usuario actualizado desde la base de datos y verificar la dirección
        updated_user = User.objects.get(pk=test_user.id)
        self.assertEqual(updated_user.domicilio, '123 Main St')