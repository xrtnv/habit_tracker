from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    is_superuser = models.BooleanField(default=False, verbose_name='администратор')
    is_staff = models.BooleanField(default=False, verbose_name='сотрудник')
    is_active = models.BooleanField(default=True, verbose_name='активный')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
