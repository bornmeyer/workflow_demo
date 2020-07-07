from rest_framework import serializers
from app.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'firstname', 'lastname', 'api_key']
        read_only_fields = ['id', 'api_key']