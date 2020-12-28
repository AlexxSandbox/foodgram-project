from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='home'),
    path('new/', views.new_recipe, name='recipe_new'),
    path('tag/<slug:slug>/', views.tag_recipes, name='recipe_tag'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),

    # path('new/', RecipeCreateView.as_view(), name='recipe_new'),
    # path('<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    # path('', RecipeListView.as_view(), name='home'),
]