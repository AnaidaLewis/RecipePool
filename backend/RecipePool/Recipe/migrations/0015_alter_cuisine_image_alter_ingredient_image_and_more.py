# Generated by Django 4.0.3 on 2022-05-10 15:43

import Recipe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0014_alter_cuisine_image_alter_ingredient_image_and_more'),
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
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=Recipe.models.upload_path_handler),
        ),
    ]
