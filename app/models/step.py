
import uuid
from django.db import models
from app.models.workflow import Workflow

class Step(models.Model):
    class Meta:
        ordering = ['order',]
        db_table = "steps"
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    description = models.TextField()
    order = models.IntegerField(default=0)

    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
