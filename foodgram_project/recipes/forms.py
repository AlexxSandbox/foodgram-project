from django import forms

from recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'image', 'tag', 'cooking_time', 'draft')
        labels = {
            'title': 'Название',
            'image': 'Изображение',
            'tag': 'Таг',
            'cooking_time': 'Время приготовления',
            'draft': 'Черновик'
        }
        help_texts = {
            'title': 'Придумай название',
            'image': 'ПРикрепи изображение',
            'tag': 'Укажи таг',
            'cooking_time': 'Уточни время приготовления',
            'draft': 'Отметь если это черновик'
        }
