from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
   honeys = models.ManyToManyField(
      'honey_app.Honey',
      related_name='users',
      help_text="Honey by user",
      through='user_honey.UserHoney',
   )
   balance = models.IntegerField(default=0)