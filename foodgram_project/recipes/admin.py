from django.contrib import admin
from django.utils.safestring import mark_safe

from recipes.models import Unit, Tag, Ingredient, Recipe, RecipeIngredients


admin.site.site_header = "FOODgram Admin"
admin.site.site_title = "FOODgram Admin Portal"
admin.site.index_title = "Welcome to most delicious portal - FOODgram"


class RecipeIngredientsInstanceInLine(admin.TabularInline):
    model = RecipeIngredients
    extra = 0


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'description', 'slug')
    readonly_fields = ('slug',)
    search_fields = ('title',)
    empty_value_display = '-пусто-'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'description', 'slug')
    readonly_fields = ('slug',)
    search_fields = ('title',)
    empty_value_display = '-пусто-'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = (('title', 'unit'), 'description', 'headshot_image', 'image', 'slug')
    search_fields = ('title', 'description')
    empty_value_display = '-пусто-'
    readonly_fields = ('headshot_image', 'slug')
    save_on_top = True

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=200,
            height=200,
            )
        )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_tags')
    fields = (
        'title',
        'tags',
        'author',
        'description',
        'headshot_image',
        'image',
        'cooking_time',
        'draft',
        'slug'
    )
    search_fields = ('title', 'description', 'author', 'ingredients')
    empty_value_display = '-пусто-'
    inlines = [RecipeIngredientsInstanceInLine]
    readonly_fields = ('headshot_image', 'slug')
    save_on_top = True

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=200,
            height=200,
            )
        )

    def get_tags(self, obj):
        return ', '.join([p.title for p in obj.tags.all()])
