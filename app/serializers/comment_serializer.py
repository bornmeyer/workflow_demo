from rest_framework import serializers
from app.models.comment import Comment

class CommentSerializer(serializers.ModelSerializer):   
    name = serializers.SerializerMethodField()    

    class Meta:
        model = Comment
        fields = ['id', 'text', 'name']
        read_only_fields = ['id']
    
    def get_name(self, obj):
        return obj.author.fullname()
   