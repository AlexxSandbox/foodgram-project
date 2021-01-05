from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from recipes.forms import RecipeForm
from recipes.models import Recipe, Tag
from users.models import User


def recipe_list(request):
    recipes = Recipe.objects.filter(draft=False)
    paginator = Paginator(recipes, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'index.html',
        {
            'page': page,
            'paginator': paginator
        }
    )


def tag_recipes(request, slug):
    tags = get_object_or_404(Tag, slug=slug)
    recipes = Recipe.objects.filter(tags=tags)
    paginator = Paginator(recipes, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'index.html',
        {
            'page': page,
            'paginator': paginator
        }
    )


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'recipes/recipe.html', {'recipe': recipe})


@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        new_recipe = form.save(commit=False)
        new_recipe.author = request.user
        new_recipe.save()
        return redirect('home')
    return render(request, 'recipes/new_recipe.html', {'form': form})


def profile(request, username):
    author = get_object_or_404(User, username=username)
    recipes = author.recipes.all()
    paginator = Paginator(recipes, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'recipes/profile.html',
        {
            'paginator': paginator,
            'page': page,
            'author': author
        }
    )
