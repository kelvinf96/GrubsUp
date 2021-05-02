from django.db import models
from accounts.models import CustomUser


class Ingredient(models.Model):
    MEAT = 'meat'
    FISH = 'fish'
    VEGETABLE = 'veg'
    GRAIN = 'grain'
    FRUIT = 'fruit'
    SPICE = 'spice'
    NUT = 'nut'
    SEED = 'seed'
    DAIRY = 'dairy'
    GRAM = 'gram'
    ML = 'ml'
    LTR = 'ltr'
    UNIT = 'unit'

    CATEGORY_CHOICES = [
        (MEAT , 'Meat'),
        (FISH, 'Fish'), 
        (VEGETABLE, 'Vegetable'),
        (GRAIN, 'Grain'), 
        (FRUIT, 'Fruit'),
        (SPICE, 'Spice'),
        (SEED, 'Seed'), 
        (DAIRY, 'Dairy'),
    ]

    UNIT_CHOICES = [
        (GRAM, 'Grams'),
        (ML, 'Ml'),
        (LTR, 'Ltr'),
        (UNIT, 'Unit'),
        ]
    
    name = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    unit = models.CharField(max_length=100, choices=UNIT_CHOICES)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    EASY = 'easy'
    INTERMEDIATE = 'intermediate'
    HARD = 'hard'

    DIFFS = [
        (EASY, 'Easy'),
        (INTERMEDIATE, 'Intermediate'),
        (HARD, 'Hard'),
    ]

    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='recipes', blank=False)
    description = models.TextField(max_length=250, blank=True)
    cooking_hours = models.PositiveIntegerField(blank=True)
    cooking_minutes = models.PositiveIntegerField(range(0,59), blank=True)
    difficulty = models.CharField(max_length=50, choices=DIFFS)
    published = models.BooleanField(editable=False, default=False)
    creator = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        default=1,
        )

    def __str__ (self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
    )
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(blank=False)

class RecipeSteps(models.Model):
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
    )
    step = models.TextField(max_length=250, blank=False)
    