import os

from django.db import models
from django.urls import reverse

from users.models import User


class CookingTime(models.TextChoices):
    HOUR = 'hours'
    MINUTE = 'minutes'


class Unit(models.Model):
    title = models.CharField('Единицы измерения', max_length=30, unique=True)
    description = models.CharField('Описание е/изм', max_length=250, blank=True, default='')
    slug = models.SlugField(unique=True)  # TODO: add prepopulated field for slug in Admin panel

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'
        ordering = ['title',]

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField('Тэг', max_length=30, unique=True)
    description = models.CharField('Описание тэга', max_length=250, blank=True, default='')
    slug = models.SlugField(unique=True) # TODO: add prepopulated field for slug in Admin panel

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title',]

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField('Ингредиент', max_length=150, unique=True)
    description = models.TextField('Описание ингредиента', blank=True, default='')
    # TODO: quantity what?
    quantity = models.PositiveSmallIntegerField('Количество', default=0)
    unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        verbose_name='Единица измерения',
        related_name='ingredients',
        blank=True,
        null=True,
    )
    # TODO: need test method to auto create filename
    image = models.ImageField(upload_to='ingredients/', blank=True, verbose_name='Изображение')
    slug = models.SlugField(unique=True) # TODO: add prepopulated field for slug in Admin panel

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['title',]

    def __str__(self):
        return self.title


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', verbose_name='Автор')
    title = models.CharField('Название', max_length=250, unique=True)
    description = models.TextField('Описание рецепта')
    # TODO: need test method to auto create filename
    image = models.ImageField(upload_to='recipes/', verbose_name='Изображение')
    ingredients = models.ManyToManyField(Ingredient, verbose_name='Игредиенты', related_name='ingredients')
    tag = models.ForeignKey(
        Tag,
        on_delete=models.SET_NULL,
        verbose_name='Таг',
        related_name='recipes',
        blank=True,
        null=True
    )
    cooking_time = models.PositiveSmallIntegerField('Время приготовления')
    time_type = models.CharField(
        'Единица времени',
        max_length=10,
        choices=CookingTime.choices,
        default=CookingTime.MINUTE
    )
    slug = models.SlugField(unique=True) # TODO: add prepopulated field for slug in Admin panel

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['title',]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.slug})


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followings',
        null=True,
        verbose_name='Подписчик',
        help_text='Автор подписки'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
        null=True,
        verbose_name='Подписан на',
        help_text='Объект подписки'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'author')


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Подписчик',
        related_name='favorites',
        help_text='автор избранного'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Подписан на',
        help_text='Рецепты в избранном'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        unique_together = ('user', 'recipe')


# TODO: create method to generate filename
def get_upload_path(instance, filename):
    path = 'recipes/'
    filename = f'{instance.title}_{instance.id}'
    return os.path.join(path, filename)
