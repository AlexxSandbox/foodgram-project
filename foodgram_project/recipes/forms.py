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
            'title': 'Укажи название рецепта',
            'image': 'Покажи как выглядит готовое блюдо',
            'tags': 'Укажи тип рецепта',
            'cooking_time': 'Укажи время приготовления в минутах',
            'draft': 'Отметь если это черновик'
        }
        widgets = {
            'tag': forms.CheckboxSelectMultiple()
        }
