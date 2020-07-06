from rest_framework import serializers
from app.models.step import Step


class StepSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Step
        fields = ['id', 'name', 'description']
        read_only_fields = ['id', 'order']
        

   