from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
class Greeting(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
