from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import DogViewSet, BreedViewSet

router = DefaultRouter()
router.register(r'dogs', DogViewSet)
router.register(r'breeds', BreedViewSet, basename='breed')

urlpatterns = [
    path('', include(router.urls)),
]