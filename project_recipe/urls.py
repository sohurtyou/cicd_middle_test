from django.contrib import admin


from django.urls import path
from recipe.views import main, recipe_detail

urlpatterns = [

    path('main/', main, name='main'),
    path('recipe_detail/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]