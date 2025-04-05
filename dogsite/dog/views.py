from django.db.models import OuterRef, Count, Subquery, Avg
from django.shortcuts import render
from rest_framework import viewsets
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()

    def get_queryset(self):

        queryset = Dog.objects.all()

        avg_age_subquery = Dog.objects.filter(
            breed=OuterRef('breed')
        ).values('breed').annotate(
            avg_age=Avg('age')
        ).values('avg_age')

        same_breed_count_subquery = Dog.objects.filter(
            breed=OuterRef('breed')
        ).values('breed').annotate(
            count=Count('id')
        ).values('count')

        if self.action == 'retrieve':
            queryset = queryset.annotate(
                same_breed_count=Subquery(same_breed_count_subquery[:1]),
            )
        else:
            queryset = queryset.annotate(
                avg_breed_age=Subquery(avg_age_subquery[:1]),
            )

        return queryset


class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()

    def get_queryset(self):
        queryset = Breed.objects.annotate(
            dog_count=Count('dogs')
        )
        return queryset
