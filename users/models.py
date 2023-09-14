from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length='150', verbose_name='Фамилия')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
