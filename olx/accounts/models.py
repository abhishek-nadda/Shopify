from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_active = models.BooleanField(default = False)
    

class Mailing(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=80)
    message=models.TextField()

    def __str__(self):
        return self.email