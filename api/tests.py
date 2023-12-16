from django.test import TestCase
from .models import Animal


class AnimalTestCase(TestCase):

   def setUp(self):
       self.lion = Animal.objects.create(name="lion", sound="roar")
       self.cat = Animal.objects.create(name="cat", sound="meow")

   def test_animals_can_speak(self):
       """Animals that can speak are correctly identified"""

       self.assertEqual(self.lion.speak(), 'The lion says "roar"')
       self.assertEqual(self.cat.speak(), 'The cat says "meow"')


class AnimalsViewTestCase(TestCase):

    def setUp(self):
       self.lion = Animal.objects.create(name="lion", sound="roar")
       self.cat = Animal.objects.create(name="cat", sound="meow")

    def test_get(self):
        response = self.client.get('/api/animals/')

        data = {
            "animals": [
                {
                    "id": 1,
                    "name": "lion",
                    "sound": "roar"
                },
                {
                    "id": 2,
                    "name": "cat",
                    "sound": "meow"
                },
            ]
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), data)

    def test_post(self):
        data = {
            "name": "dog",
            "sound": "woof"
        }
        response = self.client.post('/api/animals/', data, content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"id": 3, "name": "dog","sound": "woof"})

    def test_post_400(self):
        data = {
            "name": "dog"
        }
        response = self.client.post('/api/animals/', data, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'invalid data.'})
