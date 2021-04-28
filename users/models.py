import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_cryptography.fields import encrypt

from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager




# Create your models here.
    
class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'first_name', 'email']
    
    objects = CustomUserManager()
    # password = encrypt(models.CharField(max_length=50))
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    sc = encrypt(models.CharField(max_length=255, blank=True))
    od = encrypt(models.CharField(max_length=255, blank=True))
   
    def __str__(self):
        return f"{self.username}"
    
class Project(models.Model):
    proj_name = models.CharField(max_length=100)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='projects')
    
    def __str__(self):
        return f"{self.proj_name} by {self.user}"

class File(models.Model):
    file = models.FileField(upload_to='projects/%Y/%m/%d')
    file_name = models.CharField(max_length=255)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="files_user" )