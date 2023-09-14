from django.db import models


class CurrencyRate(models.Model):
    currency_code = models.CharField(max_length=3, unique=True)
    rate = models.DecimalField(max_digits=20, decimal_places=15)

    def __str__(self):
        return self.currency_code
