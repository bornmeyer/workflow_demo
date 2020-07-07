import uuid
from django.test import TestCase
from app.models import User
from app.models import ApiKeyAuthentication
from django.test.client import RequestFactory
from rest_framework import exceptions

class ApiKeyAuthenticationTests(TestCase):
    def setUp(self):
        api_key = uuid.uuid4()        
        User.objects.create(firstname="test", lastname="test", email="test@example.com", api_key=api_key)

    def test_that_you_can_authenticate_with_an_api_key(self):
       
        user = User.objects.get(email="test@example.com")
        user.refresh_from_db()
        url = f'/workflows'
        request_factory = RequestFactory()
        request = request_factory.get(url)
        request.query_params = {'api_key': user.api_key}
        system_under_test = ApiKeyAuthentication()

        actual, _ = system_under_test.authenticate(request)

        assert actual == user


    def test_that_an_exception_is_raise_if_api_key_is_blank(self):
      
        url = f'/workflows'
        request_factory = RequestFactory()
        request = request_factory.get(url)
        request.query_params = {}
        system_under_test = ApiKeyAuthentication()

        with self.assertRaises(exceptions.AuthenticationFailed):
            actual, _ = system_under_test.authenticate(request)

    def test_that_an_exception_is_raise_if_api_key_is_invalid(self):
      
        url = f'/workflows'
        request_factory = RequestFactory()
        request = request_factory.get(url)
        request.query_params = {'api_key': uuid.uuid4()}
        system_under_test = ApiKeyAuthentication()

        with self.assertRaises(exceptions.AuthenticationFailed):
            actual, _ = system_under_test.authenticate(request)