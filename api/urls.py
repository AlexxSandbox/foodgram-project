from django.urls import path

from api import views

urlpatterns = [
    path('v1/add_favorite/', views.add_favorite, name='add_favorite'),
    path('v1/remove_favorite/<int:recipe_id>/',
         views.remove_favorite, name='remove_favorite'),
    path('v1/add_wishlist/', views.add_wishlist, name='add_wishlist'),
    path('v1/remove_wishlist/<int:recipe_id>/',
         views.remove_wishlist, name='remove_wishlist'),
    path('v1/add_subscription/', views.add_subscription, name='add_subscription'),
    path('v1/remove_subscription/<int:following_id>/',
         views.remove_subscription, name='remove_subscription'),
    path('v1/<str:username>/<int:recipe_id>/remove/',
         views.remove_recipe, name='remove_recipe'),
    path('v1/ingredients/', views.get_ingredients, name='get_ingredients'),
    path('v1/print_cart/', views.get_cart, name='get_cart'),
]
