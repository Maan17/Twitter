from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone

class User(AbstractUser):
    pass

class post(models.Model):
    owner = models.CharField(max_length=64, default="")
    desc = models.TextField()
    post_creation_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(null=True)


