from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Breed(models.Model):
    """Модель породы собаки.

        Атрибуты:
            name (CharField): Название породы.
            size (CharField): Размер породы (Tiny, Small, Medium, Large).
            friendliness (PositiveSmallIntegerField): Уровень дружелюбия (от 1 до 5).
            trainability (PositiveSmallIntegerField): Уровень обучаемости (от 1 до 5).
            shedding_amount (PositiveSmallIntegerField): Количество линьки (от 1 до 5).
            exercise_needs (PositiveSmallIntegerField): Потребность в физических нагрузках (от 1 до 5).
    """

    SIZE_CHOICES = [
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]

    name = models.CharField(max_length=255)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendliness = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    trainability = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    shedding_amount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    exercise_needs = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        """Возвращает строковое представление породы."""

        return self.name


class Dog(models.Model):
    """Модель собаки.

        Атрибуты:
            name (CharField): Имя собаки.
            age (PositiveIntegerField): Возраст собаки в годах.
            breed (ForeignKey): Порода собаки, связанная с моделью Breed.
            gender (CharField): Пол собаки.
            color (CharField): Окрас собаки.
            favorite_food (CharField): Любимая еда собаки.
            favorite_toy (CharField): Любимая игрушка собаки.
    """

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, related_name="dogs", on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=50)
    favorite_toy = models.CharField(max_length=50)

    def __str__(self):
        """Возвращает строковое представление собаки."""

        return self.name
