import uuid
from django.test import TestCase
from app.models import User

class UserTestCase(TestCase):
    def setUp(self):
        api_key = uuid.uuid4()
        User.objects.create(firstname="Max", lastname="Mustermann", email="max@mustermann.com", api_key=api_key)
    
    def test_that_you_can_get_the_fullname(self):
        user = User.objects.get(email="max@mustermann.com")
        expected = "Max Mustermann"

        actual = user.fullname() 
        assert actual == expected