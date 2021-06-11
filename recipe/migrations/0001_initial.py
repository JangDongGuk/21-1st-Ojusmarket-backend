# Generated by Django 3.2.4 on 2021-06-11 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'recipe_categories',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image_url', models.CharField(max_length=2000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipecategory')),
            ],
            options={
                'db_table': 'recipes',
            },
        ),
    ]
