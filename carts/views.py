from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from recipes.models import Recipe


@login_required
def cart(request):
    user = request.user
    recipes = Recipe.objects.filter(recipe_cart__user=user).all()
    return render(request, 'carts/cart.html', {'recipes': recipes})
