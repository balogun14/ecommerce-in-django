from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserAccount(AbstractUser):
    profilepic = models.ImageField(upload_to='static/media')
    bio = models.TextField()
    phone = models.CharField(max_length=25, default="+234")
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=25)
    sociallinks = models.URLField()
