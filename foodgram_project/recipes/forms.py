from django import forms

from recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'image', 'tags', 'cooking_time', 'draft')
        labels = {
            'title': 'Название',
            'image': 'Изображение',
            'tags': 'Таг',
            'cooking_time': 'Время приготовления',
            'draft': 'Черновик'
        }
        help_texts = {
            'title': 'Придумай название',
            'image': 'ПРикрепи изображение',
            'tags': 'Укажи таг',
            'cooking_time': 'Уточни время приготовления',
            'draft': 'Отметь если это черновик'
        }
