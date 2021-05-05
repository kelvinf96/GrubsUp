from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('ingredients/', views.showAllIngredients, name='all_ingredients'),
    path('all/', views.showAllRecipes, name='all_recipes'),
    path('view/<int:recipe_id>/', views.singleRecipe, name='single_recipe'),
    path('add_recipe/', views.create_recipe, name='add_recipe'),
    path('my_recipes/<int:user_id>/', views.show_my_recipes, name='my_recipes'),
    path('view/<recipe_id>/add_step/', views.add_step, name='add_step'),
    path('view/<recipe_id>/add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('view/<recipe_id>/publish/', views.publish_recipe, name='publish_recipe'),
]

