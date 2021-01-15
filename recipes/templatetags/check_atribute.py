from django import template

from recipes.models import Favorite, Follow, Cart

register = template.Library()


@register.filter
def check_wishlist(recipe, user):
    check = Cart.objects.filter(
        recipe_id=recipe.id,
        user_id=user.id).exists()
    return check


@register.filter
def check_favorite(recipe, user):
    check = Favorite.objects.filter(
        recipe_id=recipe.id,
        user_id=user.id).exists()
    return check


@register.filter
def check_subscription(author, user):
    check = Follow.objects.filter(
        following=author.id,
        subscriber=user.id).exists()
    return check
