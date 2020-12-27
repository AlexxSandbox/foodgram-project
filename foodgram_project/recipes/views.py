from django.core.paginator import Paginator
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from recipes.models import Recipe


# def index(request):
#     recipe_list = Recipe.objects.filter(draft=False)
#     paginator = Paginator(recipe_list, 10)
#     page_number = request.GET.get('page')
#     page = paginator.get_page(page_number)
#     return render(request, 'indexNotAuth.html', {'page': page, 'paginator': paginator})
#     return render(request, 'indexNotAuth.html', {'recipe_list': recipe_list})


class RecipeListView(ListView):
    queryset = Recipe.objects.filter(draft=False)
    context_object_name = 'recipes'

    def get_template_names(self):
        user = self.request.user
        if user.is_authenticated:
            return 'indexAuth.html'
        return 'indexNotAuth.html'


class RecipeDetailView(DetailView):
    model = Recipe
    slug_field = 'slug'

    def get_template_names(self):
        user = self.request.user
        if user.is_authenticated:
            return 'singlePage.html'
        return 'singlePageNotAuth.html'


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'formRecipe.html'
    fields = ['title', 'description', 'image', 'tag', 'cooking_time', 'draft']
    template_name = 'formRecipe.html'
