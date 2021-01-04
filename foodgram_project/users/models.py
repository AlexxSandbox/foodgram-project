from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'admin'
    USER = 'user'


class User(AbstractUser):
    # TODO: delete field
    username = models.CharField(
        'Имя пользователя',
        max_length=50,
        blank=True,
        null=True,
        unique=True
    )
    # TODO: add error, help
    email = models.EmailField('Электронная почта', unique=True)
    bio = models.TextField('О себе', max_length=500, blank=True, null=True)
    role = models.CharField(
        'Группа доступа',
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.USER
    )
