from django.db.models import OuterRef, Count, Subquery, Avg
from django.shortcuts import render
from rest_framework import viewsets
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    """ViewSet для управления объектами Dog.

        Позволяет выполнять CRUD-операции с собаками:
        - Список всех собак с указанием среднего возраста породы.
        - Создание новой собаки.
        - Получение, обновление или удаление конкретной собаки, включая количество собак той же породы.

        Методы:
            get_queryset: Переопределение запроса с подзапросами Subquery для оптимизации.

        Attributes:
            serializer_class (DogSerializer): Сериализатор для объектов Dog.
            queryset (QuerySet): Базовый запрос к модели Dog.
    """

    serializer_class = DogSerializer
    queryset = Dog.objects.all()

    def get_queryset(self):
        """Получает оптимизированный запрос для DogViewSet.

            В списке собак добавляет информацию о среднем возрасте породы.
            При получении одной собаки — добавляет количество собак той же породы.

            Returns:
                QuerySet: Модифицированный набор данных Dog с подзапросами.
        """

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
    """ViewSet для управления объектами Breed.

        Позволяет выполнять CRUD-операции с породами:
        - Список всех пород с количеством собак каждой породы.
        - Создание новой породы.
        - Получение, обновление или удаление конкретной породы.

        Методы:
            get_queryset: Переопределение запроса с подсчётом собак через annotate.

        Attributes:
            serializer_class (BreedSerializer): Сериализатор для объектов Breed.
            queryset (QuerySet): Базовый запрос к модели Breed.
    """

    serializer_class = BreedSerializer
    queryset = Breed.objects.all()

    def get_queryset(self):
        """Получает оптимизированный запрос для BreedViewSet.

            Возвращает список пород с подсчитанным количеством собак для каждой породы.

            Returns:
                QuerySet: Модифицированный набор данных Breed с подсчётом собак.
        """

        queryset = Breed.objects.annotate(
            dog_count=Count('dogs')
        )
        return queryset
