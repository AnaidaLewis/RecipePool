# Generated by Django 4.0.3 on 2022-05-10 14:53

import Recipe.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Recipe', '0013_rename_recipe_recipe_cuisine_alter_cuisine_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=Recipe.models.upload_path_handler),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='image',
            field=models.ImageField(upload_to=Recipe.models.upload_path_handler),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='createdBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to=Recipe.models.upload_path_handler),
        ),
    ]
