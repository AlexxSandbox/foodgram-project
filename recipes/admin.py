from django.contrib import admin
from django.utils.safestring import mark_safe

from recipes.models import Ingredient, Recipe, RecipeIngredients


admin.site.site_header = "FOODgram Admin"
admin.site.site_title = "FOODgram Admin Portal"
admin.site.index_title = "Welcome to most delicious portal - FOODgram"


class RecipeIngredientsInstanceInLine(admin.TabularInline):
    model = RecipeIngredients
    extra = 0


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'description', 'dimension')
    search_fields = ('title', 'description')
    empty_value_display = '-пусто-'
    save_on_top = True


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = (
        'title',
        'tags',
        'author',
        'description',
        'headshot_image',
        'image',
        'cooking_time'
    )
    search_fields = ('title', 'description', 'author', 'ingredients')
    empty_value_display = '-пусто-'
    inlines = [RecipeIngredientsInstanceInLine]
    readonly_fields = ('headshot_image',)
    save_on_top = True

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=200,
            height=200,
            )
        )
