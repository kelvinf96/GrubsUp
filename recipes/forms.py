from django import forms
from . import models

class RecipeForm(forms.ModelForm):
    class Meta:
        model = models.Recipe
        exclude = ['published', 'creator']
    

class StepForm(forms.ModelForm):
    class Meta:
        model = models.RecipeSteps
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.RecipeIngredient
        fields = '__all__'


