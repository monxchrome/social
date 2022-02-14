from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
import uuid
from users.managers import UserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    last_name = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phones = models.CharField(null=True, blank=True, verbose_name=('phone'), max_length=32)
    is_staff = models.BooleanField(default=False, verbose_name=_('teacher'))

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager