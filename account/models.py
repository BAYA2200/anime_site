from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
