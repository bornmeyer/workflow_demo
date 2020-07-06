from app.models.user import User
from rest_framework import authentication
from rest_framework import exceptions

class ApiKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print("test")
        api_key = request.query_params.get('api_key')
        print(not api_key)
        if not api_key:
            raise exceptions.AuthenticationFailed('No such key')

        try:
            user = User.objects.get(api_key=api_key)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)