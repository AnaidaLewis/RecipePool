# Generated by Django 4.0.3 on 2022-05-16 13:04

import Recipe.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('cuisine_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=Recipe.models.upload_path_handler)),
                ('likes', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=Recipe.models.upload_path_handler)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('instructions', models.TextField(max_length=255)),
                ('totalTime', models.TimeField()),
                ('url', models.URLField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=Recipe.models.upload_path_handler)),
                ('healthLabels', models.CharField(max_length=100)),
                ('totalNutrients', models.CharField(max_length=100)),
                ('calories', models.IntegerField()),
                ('cuisineType', models.CharField(max_length=50)),
                ('mealType', models.CharField(max_length=50)),
                ('dishType', models.CharField(max_length=50)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('missingIngredients', models.CharField(blank=True, max_length=100, null=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_user', to=settings.AUTH_USER_MODEL)),
                ('cuisine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_cuisine', to='Recipe.cuisine')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_likes', to='Recipe.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.CreateModel(
            name='IngredientList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=1.0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredient', to='Recipe.ingredient')),
                ('recipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_list', to='Recipe.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_fav', to='Recipe.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_fav', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
