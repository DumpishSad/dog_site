from rest_framework import serializers
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Breed.

        Добавляет количество собак данной породы (dog_count).

        Attributes:
            dog_count (IntegerField): Количество собак определенной породы (только для чтения).
    """

    dog_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = [
            "id",
            "name",
            "size",
            "friendliness",
            "trainability",
            "shedding_amount",
            "exercise_needs",
            "dog_count",
        ]


class DogSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Dog.

        Добавляет:
        - Название породы (breed_name).
        - Количество собак той же породы (same_breed_count).
        - Средний возраст собак породы (avg_breed_age).

        Attributes:
            breed_name (CharField): Название породы собаки (только для чтения).
            same_breed_count (IntegerField): Количество собак той же породы (только для чтения).
            avg_breed_age (FloatField): Средний возраст собак этой породы (только для чтения).
    """

    breed_name = serializers.CharField(source="breed.name", read_only=True)
    same_breed_count = serializers.IntegerField(read_only=True)
    avg_breed_age = serializers.FloatField(read_only=True)

    class Meta:
        model = Dog
        fields = [
            "id",
            "name",
            "age",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
            "breed",
            "breed_name",
            "same_breed_count",
            "avg_breed_age",
        ]
