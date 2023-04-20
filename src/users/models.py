from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import UserManager


# Create your models here.

class CustomUser(AbstractUser):
    # add additional fields in here
    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username
