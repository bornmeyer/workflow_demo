from rest_framework import serializers
from app.models.step import Step


class StepSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Step
        fields = ['id', 'name', 'description']
        read_only_fields = ['id', 'order']
        

    def create(self, validated_data):
        print(dict(validated_data))
        new_step = Step(**validated_data)
        new_step.save(force_insert=True)
        
        return new_step