# Generated by Django 3.1.3 on 2020-12-26 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20201226_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counts',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient', verbose_name='Ингредиенты'),
        ),
    ]
