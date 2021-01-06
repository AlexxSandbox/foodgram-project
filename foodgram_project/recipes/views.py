from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from recipes.forms import RecipeForm
from recipes.models import Recipe
from users.models import User


def recipe_list(request):
    tag = request.GET.get('tag')
    if tag is not None:
        recipes = Recipe.objects.prefetch_related('tags').filter(
            draft=False,
            tags__slug=tag
        )
    else:
        recipes = Recipe.objects.filter(draft=False)

    paginator = Paginator(recipes, 9)
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
    tag = request.GET.get('tag')

    if tag is not None:
        recipes = author.recipes.prefetch_related('tags').filter(tags__slug=tag)
    else:
        recipes = author.recipes.all()

    paginator = Paginator(recipes, 9)
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


def page_not_found(request, exception):
    return render(request, 'misc/404.html', {'path': request.path}, status=404)


def server_error(request):
    return render(request, 'misc/500.html', status=500)
