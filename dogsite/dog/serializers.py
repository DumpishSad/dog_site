from rest_framework import serializers
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
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
