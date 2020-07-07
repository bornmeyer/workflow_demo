import uuid
from rest_framework import serializers
from app.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'firstname', 'lastname', 'api_key']
        read_only_fields = ['id', 'api_key']

    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.api_key = str(uuid.uuid4())
        new_user.save(force_insert=True)
        return new_user