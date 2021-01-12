from django.db import models
from django.contrib.auth import get_user_model

from recipes.models import Recipe

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber_cart'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_cart'
    )
