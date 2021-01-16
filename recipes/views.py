import operator
from functools import reduce

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from recipes.forms import RecipeForm
from recipes.models import Recipe, TAGS_CHOICES, RecipeIngredients

User = get_user_model()


def get_ingredients(request):
    ingredients = {}
    for key, value in request.POST.items():
        if key.startswith('nameIngredient_'):
            arg = key.split('_')[1]
            title = value
            amount = request.POST['valueIngredient_' + arg]
            ingredients[title] = amount
        continue
    return ingredients


def tag_collect(request):
    tags = []
    tags_filter = None
    for label, _ in TAGS_CHOICES:
        if request.GET.get(label, ''):
            tags.append(label)
    if tags:
        tags_filter = reduce(
            operator.or_, (Q(tags__contains=tag)for tag in tags))
    return tags, tags_filter
home

def index(request):
    tags, tags_filter = tag_collect(request)
    if tags_filter:
        recipes = Recipe.objects.filter(tags_filter).all()
    else:
        recipes = Recipe.objects.all()
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'paginator': paginator,
        'tags': tags
    }
    return render(request, 'index.html', context)


def user_page(request, username):
    author = get_object_or_404(User, username=username)
    tags, tags_filter = tag_collect(request)
    if tags_filter:
        recipes = Recipe.objects.filter(tags_filter).filter(
            author_id=author.id).all()
    else:
        recipes = Recipe.objects.filter(author_id=author.id)
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'paginator': paginator,
        'tags': tags,
        'author': author
    }
    return render(request, 'recipes/user_page.html', context)


def recipe_page(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author__username=username)
    author = recipe.author
    ingredients = recipe.recipeingredients_set.all()
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
        'author': author
    }
    return render(request, 'recipes/recipe_page.html', context)


@login_required
def feed(request):
    user = request.user
    authors = User.objects.filter(
        following__subscriber=user).prefetch_related('recipes')
    paginator = Paginator(authors, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'authors': authors,
        'page': page,
        'paginator': paginator
    }
    return render(request, 'recipes/feed.html', context)


@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)

    if request.method == 'POST':
        ingredients = get_ingredients(request)

        if not ingredients:
            form.add_error(None, 'Должен быть хотя бы один ингредиент')

        elif form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            for title, amount in ingredients.items():
                RecipeIngredients.add_ingredient(recipe, title, amount)
            return redirect('index')

    form = RecipeForm()
    context = {'form': form}
    return render(request, 'recipes/form_recipe.html', context)


@login_required
def edit_recipe(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author__username=username)
    recipe_redirect = redirect('recipe', username=username, recipe_id=recipe_id)

    if request.user != recipe.author:
        return recipe_redirect

    is_breakfast = 'breakfast' in recipe.tags
    is_lunch = 'lunch' in recipe.tags
    is_dinner = 'dinner' in recipe.tags
    ingredients = RecipeIngredients.objects.filter(recipe_id=recipe_id)

    form = RecipeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=recipe
    )
    if form.is_valid():
        new_ingredients = get_ingredients(request)
        RecipeIngredients.objects.filter(recipe_id=recipe).delete()
        recipe = form.save(commit=False)
        recipe.author = request.user
        form.save()
        for title, amount in new_ingredients.items():
            RecipeIngredients.add_ingredient(recipe, title, amount)
        return recipe_redirect

    context = {
        'form': form,
        'recipe': recipe,
        'is_breakfast': is_breakfast,
        'is_lunch': is_lunch,
        'is_dinner': is_dinner,
        'ingredients': ingredients
    }
    return render(request, 'recipes/form_recipe.html', context)


@login_required
def favorites(request):
    user = request.user
    tags, tags_filter = tag_collect(request)
    if tags_filter:
        recipes = Recipe.objects.filter(tags_filter).filter(
            favorite_recipe__user=user).all()
    else:
        recipes = Recipe.objects.filter(
            favorite_recipe__user=user).all()
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'paginator': paginator,
        'tags': tags
    }
    return render(request, 'recipes/favorites.html', context)


@login_required
def cart(request):
    user = request.user
    recipes = Recipe.objects.filter(recipe_cart__user=user)
    return render(request, 'recipes/cart.html', {'recipes': recipes})


def page_not_found(request, exception):
    return render(request, 'misc/404.html', {'path': request.path}, status=404)


def server_error(request):
    return render(request, 'misc/500.html', status=500)
