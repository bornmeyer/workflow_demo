from rest_framework import viewsets
from app.serializers.user_serializer import UserSerializer
from app.models.user import User

"""
Provides methods to manipulate user resources, accessible via /users

A get returns a list of all users,

A post creates a new user

"""
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    authentication_classes = []
    permission_classes = []
