from django.db import models
from django.contrib.auth.models import User
import uuid
from cryptography.fernet import Fernet
from django.conf import settings

f = Fernet(settings.ENCRYPTION_KEY)
# Create your models )here.
class ex_accounts(models.Model):
    id = models.UUIDField(primary_key= True,default=uuid.uuid4,editable=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    UserName = models.BinaryField(max_length=100)
    Password = models.BinaryField(max_length=100)
    bio = models.BinaryField(max_length=10)
    
    @property
    def decrypt_UserName(self):
        return f.decrypt(self.UserName).decode('utf-8')
    @property
    def decrypt_Password(self):
        return f.decrypt(self.Password).decode('utf-8')
    @property
    def decrypt_bio(self):
        return f.decrypt(self.bio).decode('utf-8')
        

    def __str__(self):
        return f.decrypt(self.bio).decode('utf-8')

