from rest_framework import serializers
from app.models.workflow import Workflow
from app.serializers.step_serializer import StepSerializer
from app.serializers.comment_serializer import CommentSerializer

class WorkflowSerializer(serializers.ModelSerializer):
    steps = StepSerializer(source='step_set', many=True, read_only=True)
    comments = CommentSerializer(source='comment_set', many=True, read_only=True)
    class Meta:
        model = Workflow
        fields = ['id', 'name', 'description', 'steps', 'comments']
        read_only_fields = ['id']
        