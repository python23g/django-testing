from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status



class AnimalViewTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='ali')
        self.user.set_password('1234')
        self.user.save()
        self.client.force_authenticate(self.user)

    def test_animals(self):
        response = self.client.get('/api/animals/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
