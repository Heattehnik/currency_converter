from django.urls import path
from .views import CurrencyConversionView

urlpatterns = [
    path('rates/', CurrencyConversionView.as_view(), name='currency-conversion'),
]
