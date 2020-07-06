
import uuid
from django.db import models

class User(models.Model):
    db_table = "users"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    firstname = models.TextField(default="")
    lastname = models.TextField(default="")
    api_key = models.TextField(default="")