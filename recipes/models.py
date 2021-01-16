from django.contrib.auth import get_user_model
from django.db import models
from multiselectfield import MultiSelectField
from pytils.translit import slugify

User = get_user_model()

TAGS_CHOICES = (('breakfast', 'Завтрак'),
               ('lunch', 'Обед'),
               ('dinner', 'Ужин'))


class Ingredient(models.Model):
    title = models.CharField('Ингредиент', max_length=150, unique=True)
    description = models.TextField(
        'Описание ингредиента',
        blank=True,
        default=''
    )
    dimension = models.CharField(
        max_length=25,
        verbose_name='Единица измерения'
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['title', ]

    def __str__(self):
        return f"{self.title} / {self.dimension}"


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    title = models.CharField(
        'Название рецепта',
        max_length=150,
        unique=True
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='recipes/',
        verbose_name='Изображение'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Игредиенты',
        through='RecipeIngredients'
    )
    tags = MultiSelectField(
        choices=TAGS_CHOICES,
        blank=True,
        null=True,
        verbose_name='Теги'
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления,мин',
        default=0
    )

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['title', ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)


class RecipeIngredients(models.Model):
    amount = models.PositiveIntegerField(verbose_name='Количество')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )


class Follow(models.Model):
    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Подписчик',
        help_text='Автор подписки'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписан на',
        help_text='Объект подписки'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='favorite_subscriber',
        help_text='автор избранного'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite_recipe',
        verbose_name='Подписан на',
        help_text='Рецепты в избранном'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber_cart'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_cart'
    )
