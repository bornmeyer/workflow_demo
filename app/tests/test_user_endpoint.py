import uuid
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import User

class UserEndpointTests(APITestCase):
    def setUp(self):
        User.objects.all().delete()
        api_key = uuid.uuid4()
        User.objects.create(firstname="Max", lastname="Mustermann", email="max@mustermann.com", api_key=api_key)

    def test_that_you_can_create_a_user(self):
        data = {
            'email': 'test@test.com',
            'firstname': 'test',
            'lastname': 'test'
        }

        requesting_user = User.objects.get(email="max@mustermann.com")
        url = f"/users/?api_key={requesting_user.api_key}"
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(User.objects.get(email="test@test.com"))