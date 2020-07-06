import uuid
from rest_framework import serializers
from app.models.comment import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'text']
        read_only_fields = ['id']