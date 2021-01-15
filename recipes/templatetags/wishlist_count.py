from django import template

from recipes.models import Cart

register = template.Library()


@register.filter
def wishlist_count(user):
    return Cart.objects.filter(user_id=user.id).count()
