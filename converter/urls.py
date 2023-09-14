from rest_framework.routers import DefaultRouter
from django.urls import path
from .apps import ConverterConfig
from .views import RatesViewSet

app_name = ConverterConfig.name

router = DefaultRouter()
router.register(r"api", RatesViewSet, basename="api")

urlpatterns = [
    path("api/rates/", RatesViewSet.as_view({'get': 'convert_currency'}), name="convert-currency"),  # Маршрут для конвертации валюты
]

urlpatterns += router.urls  # Включаем URL-маршруты, созданные DefaultRouter
