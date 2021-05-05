from django.shortcuts import render
from . import models
from .forms import RecipeForm, StepForm, IngredientForm
from django.http import HttpResponseRedirect

def showAllIngredients(request):
    ingredients = models.Ingredient.objects.all()

    return render(request, 'ingredients.html', {'ingredients': ingredients})

def showAllRecipes(request):
    all_recipes = models.Recipe.objects.filter(published=True)

    return render(request, 'recipes.html', {'all_recipes': all_recipes})

def singleRecipe(request, recipe_id):
    requested_recipe = models.Recipe.objects.filter(id=recipe_id)
    recipe_steps = models.RecipeSteps.objects.filter(recipe=recipe_id)
    recipe_ingredient = models.RecipeIngredient.objects.filter(recipe=recipe_id)

    return render(request, 'recipe_details.html', {'requested_recipe': requested_recipe, 'recipe_steps':recipe_steps,
    'recipe_ingredient':recipe_ingredient})

def create_recipe(request):

    c_user = request.user

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = c_user
            obj.save()
            return HttpResponseRedirect('/home/')
    else:
        form = RecipeForm()
    
    return render(request, 'add_recipe.html', {'form': form})

def show_my_recipes(request, user_id):
    my_recipes = models.Recipe.objects.filter(creator=user_id)

    return render(request, 'my_recipes.html', {'my_recipes': my_recipes})

def add_step(request, recipe_id):
    if request.method == 'POST':
        form = StepForm(request.POST)
        base_url = 'recipes/' + str(recipe_id)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/recipes/view/' + str(recipe_id))

    else:
        form = StepForm()

    return render(request, 'add_step.html', {'form': form, 'recipe_id': recipe_id})

def add_ingredient(request, recipe_id):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/recipes/view/' + str(recipe_id))

    else:
        form = IngredientForm()

    return render(request, 'add_ingredient.html', {'form': form, 'recipe_id': recipe_id})

def publish_recipe(request, recipe_id):
    recipe_to_pub = models.Recipe.objects.get(id=recipe_id)
    recipe_to_pub.published=True
    recipe_to_pub.save()

    return HttpResponseRedirect('/recipes/view/' + str(recipe_id))