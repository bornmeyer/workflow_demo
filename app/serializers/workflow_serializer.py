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
        

    def create(self, validated_data):            
        new_workflow = Workflow(**validated_data)
        new_workflow.save(force_insert=True)        
        return new_workflow