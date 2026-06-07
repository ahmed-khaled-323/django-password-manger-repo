from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class ex_accounts(models.Model):
    id = models.UUIDField(primary_key= True,default=uuid.uuid4,editable=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    bio = models.CharField(max_length=10)
    def __str__(self):
        return self.bio

