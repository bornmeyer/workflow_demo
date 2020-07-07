
import uuid
from django.db import models

class User(models.Model):
    class Meta:
        db_table = "users"
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique email')
        ]
    
   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    firstname = models.TextField(default="")
    lastname = models.TextField(default="")
    api_key = models.TextField(default="")

    
    def fullname(self):
        return f"{self.firstname} {self.lastname}"