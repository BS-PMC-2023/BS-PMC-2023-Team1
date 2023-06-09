from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase, Client

from home_page.views import generateGraph
from registration.models import UserData
from articles.models import PredictionApproves, ArticleCache


class Viewtest(TestCase):
    def setUp(self):
        # Set up any necessary objects or data required for the tests
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_data = UserData.objects.create(user=self.user)

    def test_generateGraph(self):
        # Write test cases for the generateGraph function
        # Example:
        # 1. Test the function with valid inputs and check if it returns the expected result
        # 2. Test the function with invalid inputs and check if it handles the errors correctly

        # Example test case:
        image_base64 = generateGraph(self.user.username, self.user.id)
        self.assertTrue(image_base64)  # Check if the returned image_base64 is not empty

    def test_home_view(self):
        # Write test cases for the home view
        # Example:
        # 1. Test if the view returns a 200 status code (OK)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view2(self):
        # Write test cases for the home view
        # Example:
        # 1. Test if the view returns a 200 status code (OK)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_myarticle_view(self):
        # Write test cases for the myarticle view
        # Example:
        # 1. Test if the view returns a 200 status code (OK)
        # 2. Test if the view passes the expected context data to the template

        # Example test case:
        response = self.client.get(reverse('myarticle'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('articles', response.context)

    # Add more test methods for other views as needed
    def test_expertArticleList_view(self):
        # Write test cases for the expertArticleList view
        # Example:
        # 1. Test if the view returns a 200 status code (OK)
        # 2. Test if the view passes the expected context data to the template

        # Example test case:
        response = self.client.post(reverse('expertArticleList'), {'expertId': self.user.id})
        self.assertEqual(response.status_code, 200)
        self.assertIn('articles', response.context)

    def test_myProfile_view(self):
        # Write test cases for the myProfile view
        # Example:
        # 1. Test if the view returns a 200 status code (OK)
        # 2. Test if the view passes the expected context data to the template

        # Example test case:
        response = self.client.get(reverse('myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.context)

    def test_myProfile_post(self):
        # Write test cases for the myProfile view when submitting a POST request
        # Example:
        # 1. Test if the view correctly updates the user's profile information in the database
        # 2. Test if the view handles different scenarios (e.g., missing fields, invalid passwords) correctly

        # Example test case:
        response = self.client.post(reverse('myProfile'), {'firstname': 'SOME STRING'})
        self.assertEqual(response.status_code, 200)

        # Check if the user's profile information was updated correctly
        updated_user_data = UserData.objects.get(user=self.user)
        self.assertEqual(updated_user_data.firstname, 'SOME STRING')

    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_myProfile_url(self):
        response = self.client.get(reverse('myProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myProfile.html')

    def test_myarticle_url(self):
        response = self.client.get(reverse('myarticle'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myarticle.html')

    def test_expertArticleList_url(self):
        response = self.client.post(reverse('expertArticleList'), {'expertId': self.user.id})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myarticle.html')


