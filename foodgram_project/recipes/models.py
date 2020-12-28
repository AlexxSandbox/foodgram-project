import os
import re

from django.db import models
from pytils.translit import slugify
from django.urls import reverse

from users.models import User


def get_upload_path(instance, filename):
    """
    generate filename by title and class name
    """
    path = f'{instance.__class__.__name__}/'
    t = re.search('\.(.+)$', filename).group(1)
    filename = f'{str(instance.slug)}.{t}'
    return os.path.join(path, filename)


class Unit(models.Model):
    title = models.CharField('Единицы измерения', max_length=30, unique=True)
    description = models.CharField('Описание', max_length=50, blank=True,
                                   default='')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'
        ordering = ['title', ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Unit, self).save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField('Тэг', max_length=10, unique=True)
    description = models.CharField('Описание тэга', max_length=50, blank=True,
                                   default='')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title', ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


class Ingredient(models.Model):
    title = models.CharField('Ингредиент', max_length=150, unique=True)
    description = models.TextField('Описание ингредиента', blank=True,
                                   default='')
    unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_DEFAULT,
        verbose_name='Единица измерения',
        related_name='ingredients',
        default=''
    )
    image = models.ImageField(upload_to=get_upload_path, blank=True,
                              verbose_name='Изображение')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['title', ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Ingredient, self).save(*args, **kwargs)


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    title = models.CharField('Название', max_length=150, unique=True)
    description = models.TextField('Описание рецепта')
    image = models.ImageField(upload_to=get_upload_path,
                              verbose_name='Изображение')
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Игредиенты',
        through='RecipeIngredients'
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Таг',
        related_name='recipes'
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления, мин',
        default=0
    )
    slug = models.SlugField(unique=True)
    draft = models.BooleanField('Черновик', default=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['title', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField('Количество', default=0)

    class Meta:
        verbose_name = 'Состав рецепта'
        verbose_name_plural = 'Состав рецепта'


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
