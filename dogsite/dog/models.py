from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Breed(models.Model):
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
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, related_name="dogs", on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=50)
    favorite_toy = models.CharField(max_length=50)

    def __str__(self):
        return self.name
