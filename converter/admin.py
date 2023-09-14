from django.contrib import admin
from converter.models import CurrencyRate


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    pass
