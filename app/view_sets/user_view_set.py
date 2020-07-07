from rest_framework import viewsets
from app.serializers.user_serializer import UserSerializer
from app.models.user import User
from rest_framework.decorators import authentication_classes, api_view

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    authentication_classes = []
    permission_classes = []
