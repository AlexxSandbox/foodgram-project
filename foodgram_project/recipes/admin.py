from django.contrib import admin

from recipes.models import Unit, Tag, Ingredient, Recipe


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', )
    empty_value_display = '-пусто-'


@admin.register(Tag)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', )
    empty_value_display = '-пусто-'


@admin.register(Ingredient)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'unit', 'image', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'description')
    empty_value_display = '-пусто-'


@admin.register(Recipe)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'title',
        'description',
        'image',
        'ingredients',
        'tag',
        'cooking_time',
        'time_type',
        'slug'
    )
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'description', 'author', 'ingredients')
    empty_value_display = '-пусто-'
