from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserData
from .forms import UserRegisterForm
from favoriteExpert.models import favoriteExpert


class UserRegistrationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_user(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'firstname': 'Test',
            'lastname': 'User',
            'isexpert': True,
            'pic': '',
            'Certificate': '',
            'isAdmin': False
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertTrue(UserData.objects.filter(user__username='testuser').exists())


class UserLoginTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.register_url = reverse('register')

        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_login_success(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_login_failure(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_valid_form(self):
        form_data = {
            'username': 'testuser2',
            'email': 'testuserexample.com',
            'password1': 'password123',
            'password2': 'password123',
            'firstname': 'John',
            'lastname': 'Doe',
        }

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
            'firstname': 'John',
            'lastname': '',  # missing required field
        }

        form = UserRegisterForm(data=form_data)

        self.assertFalse(form.is_valid())

        self.assertIn('lastname', form.errors)


from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


#######################integration tests#####################3
class UserRegistrationLoginTest2(TestCase):
    def test_user_registration_login(self):
        # Register a new user
        register_url = reverse('register')
        register_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'firstname': 'Test',
            'lastname': 'User',
            'isexpert': False,
            'Certificate': '',
            'isAdmin': False
        }
        response = self.client.post(register_url, register_data)
        self.assertEqual(response.status_code, 302)  # Redirect to home page

        # Log in with the registered user
        login_url = reverse('login')
        login_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(login_url, login_data)
        self.assertEqual(response.status_code, 302)  # Redirect to home page
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Ensure the user is logged in

        # Ensure the user is logged in

    def test_user_registration_login2(self):
        # Register a new user
        register_url = reverse('register')
        register_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'firstname': 'Test',
            'lastname': 'User',
            'isexpert': True,
            'Certificate': '',
            'isAdmin': True
        }
        response = self.client.post(register_url, register_data)
        self.assertEqual(response.status_code, 302)  # Redirect to home page

        # Log in with the registered user
        login_url = reverse('login')
        login_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(login_url, login_data)
        self.assertEqual(response.status_code, 200)  # Redirect to home page
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_user_registration_login3(self):
        # Register a new user
        register_url = reverse('register')
        register_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'firstname': 'Test',
            'lastname': 'User',
            'isexpert': True,
            'Certificate': '',
            'isAdmin': False
        }
        response = self.client.post(register_url, register_data)
        self.assertEqual(response.status_code, 302)  # Redirect to home page

        register_url = reverse('register')
        register_data = {
            'username': 'testuser2',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'firstname': 'Test',
            'lastname': 'User',
            'isexpert': False,
            'Certificate': '',
            'isAdmin': False
        }
        response = self.client.post(register_url, register_data)
        self.assertEqual(response.status_code, 200)  # Redirect to home page

        # Log in with the registered user
        login_url = reverse('login')
        login_data = {
            'username': 'testuser2',
            'password': 'testpassword'
        }
        response = self.client.post(login_url, login_data)
        self.assertEqual(response.status_code, 200)  # Redirect to home page

        # Like a user
        User.objects.create_user(username='testuser2', password='testpassword')
        UserData.objects.create(user_id=2, firstname='testuser2', lastname='testuser2', isexpert=False)
        user_id = User.objects.get(username='testuser2').id

        User.objects.create_user(username='testuse33333333r', password='testpassword')
        UserData.objects.create(user_id=3, firstname='testuser', lastname='testuser', isexpert=False)
        user_id2 = User.objects.get(username='testuser').id
        expert_id = UserData.objects.get(user_id=user_id).id
        # Create a favoriteExpert object
        favoriteExpert.objects.create(expertId=expert_id, userId=user_id)

        self.assertEqual(favoriteExpert.objects.count(), 1)  # Verify the object is created


    def test_user_registration_login4(self):
        # Register a new user
        register_url = reverse('register')
        register_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'firstname': 'Test',
            'lastname': 'User',
            'isexpert': True,
            'Certificate': '',
            'isAdmin': False
        }
        response = self.client.post(register_url, register_data)
        self.assertEqual(response.status_code, 302)  # Redirect to home page

        register_url = reverse('register')
        register_data = {
            'username': 'testuser2',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'firstname': 'Test',
            'lastname': 'User',
            'isexpert': False,
            'Certificate': '',
            'isAdmin': False
        }
        response = self.client.post(register_url, register_data)
        self.assertEqual(response.status_code, 200)  # Redirect to home page

        # Log in with the registered user
        login_url = reverse('login')
        login_data = {
            'username': 'testuser2',
            'password': 'testpassword'
        }
        response = self.client.post(login_url, login_data)
        self.assertEqual(response.status_code, 200)  # Redirect to home page

        # Like a user
        User.objects.create_user(username='testuser2', password='testpassword')
        UserData.objects.create(user_id=2, firstname='testuser2', lastname='testuser2', isexpert=False)
        user_id = User.objects.get(username='testuser2').id

        User.objects.create_user(username='testuse33333333r', password='testpassword')
        UserData.objects.create(user_id=3, firstname='testuser', lastname='testuser', isexpert=False)
        user_id2 = User.objects.get(username='testuser').id
        expert_id = UserData.objects.get(user_id=user_id).id
        # Create a favoriteExpert object

        self.assertNotEquals(favoriteExpert.objects.count(), 1)  # Verify the object is created

