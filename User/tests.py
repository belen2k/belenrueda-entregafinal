from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Avatar
from .forms import UserRegisterForm, UserEditForm




class UserAuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_register_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
        })
        
        print(f"Response: {response.status_code}")  # Verifica si se redirige (302)
        
        self.assertEqual(response.status_code, 302)  # Verifica que se redirija
        self.assertTrue(User.objects.filter(username='newuser').exists())  # Verifica que el usuario esté creado

    def test_login_user(self):
        # Realizar la solicitud POST para iniciar sesión con un usuario válido
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass',
        })
        # Verifica que la redirección tras el inicio de sesión sea exitosa
        self.assertEqual(response.status_code, 302)

    def test_logout_user(self):
        # Iniciar sesión con el usuario de prueba
        self.client.login(username='testuser', password='testpass')
        # Realizar la solicitud POST para cerrar sesión
        response = self.client.post(reverse('cerrar_sesion'))
        # Verifica que la redirección tras el cierre de sesión sea exitosa
        self.assertEqual(response.status_code, 302)