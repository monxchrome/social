from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractBaseUser):
    date_of_birth = models.DateField()
    height = models.FloatField()

    REQUIRED_FIELDS = ['date_of_birth', 'height']