# Generated by Django 3.2 on 2021-05-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='creator',
            field=models.CharField(default='kelvoj96', editable=False, max_length=100),
        ),
    ]
