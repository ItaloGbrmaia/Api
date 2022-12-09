from django.db import models
from uuid import uuid4

class User(models.Model):
    
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=244)
    last_name = models.CharField(max_length=244)
    email = models.EmailField(("E-Mail"), max_length=254)
    old = models.IntegerField()
    phone = models.CharField(max_length=24)
    