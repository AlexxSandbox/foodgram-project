from django.urls import path

from recipes import views


urlpatterns = [
    path('', views.recipe_list, name='home'),
    path('new/', views.new_recipe, name='recipe_new'),
    path('<str:username>/', views.profile, name='profile'),
    path('detail/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]
