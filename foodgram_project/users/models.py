from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'admin'
    USER = 'user'


class User(AbstractUser):
    username = models.CharField(
        'Логин',
        max_length=150,
        unique=True,
        help_text='Используется для входа на сайт'
    )
    first_name = models.CharField('Имя', max_length=150)
    last_name = models.CharField('Фамилия', max_length=150)
    email = models.EmailField(
        'Электронная почта',
        unique=True,
        help_text='Ипользуется для восстановления пароля'
    )
    bio = models.TextField('О себе', max_length=500, default='', blank=True)
    role = models.CharField(
        'Группа доступа',
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.USER
    )
