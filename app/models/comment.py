import uuid
from django.db import models
from .user import User
from .workflow import Workflow

class Comment(models.Model):
    class Meta:
        db_table = "comments"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #name = models.TextField()
    text = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)