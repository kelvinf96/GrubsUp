from django.shortcuts import render
from . import models
from .forms import RecipeForm
from django.http import HttpResponseRedirect

def showAllIngredients(request):
    ingredients = models.Ingredient.objects.all()

    return render(request, 'ingredients.html', {'ingredients': ingredients})

def showAllRecipes(request):
    all_recipes = models.Recipe.objects.filter(published=True)

    return render(request, 'recipes.html', {'all_recipes': all_recipes})

def singleRecipe(request, recipe_id):
    requested_recipe = models.Recipe.objects.filter(id=recipe_id)

    return render(request, 'recipe_details.html', {'requested_recipe': requested_recipe})

def create_recipe(request):

    c_user = request.user

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        form.creator = c_user.username

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = RecipeForm()
    
    return render(request, 'add_recipe.html', {'form': form})