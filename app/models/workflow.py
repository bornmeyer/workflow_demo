import uuid
from django.db import models
from .user import User

class Workflow(models.Model):
    class Meta:        
        db_table = "workflows"
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    description = models.TextField()
    order = models.IntegerField(default=0)

    #parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='steps')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)