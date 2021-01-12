from django.urls import path

from recipes import views


urlpatterns = [
    path('', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
    path('new/', views.new_recipe, name='new'),
    path('favorites/', views.favorites, name='favorites'),
    path('<username>/', views.user_page, name='user'),
    path('<username>/<int:recipe_id>/', views.recipe_page, name='recipe'),
    path('<username>/<recipe_id>/edit/', views.edit_recipe, name='edit_recipe')
]
