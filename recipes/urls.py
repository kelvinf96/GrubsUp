from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('ingredients/', views.showAllIngredients, name='all_ingredients'),
    path('all/', views.showAllRecipes, name='all_recipes'),
    path('view/<int:recipe_id>/', views.singleRecipe, name='single_recipe'),
    path('add_recipe/', views.create_recipe, name='add_recipe'),
]

