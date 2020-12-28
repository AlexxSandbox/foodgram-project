from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class CustomUserCreationForm(UserCreationForm):
    model = User
    fields = ('username', 'email')
