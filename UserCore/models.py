from django.db import models

# Create your models here.
class USERS(models.Model):

    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=10)

    def __str__(self):
        return self.UserName