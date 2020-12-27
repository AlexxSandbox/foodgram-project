from django.urls import path
from . import views
from .views import RecipeListView, RecipeDetailView, RecipeCreateView

urlpatterns = [
    # path('', views.index, name='index'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe_new'),
    path('recipe/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('', RecipeListView.as_view(), name='home'),
]