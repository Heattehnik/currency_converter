from celery import shared_task
from _decimal import Decimal
import requests
from converter.models import CurrencyRate


@shared_task
def get_currencies():
    """
    Getting the exchange rate of the Central Bank of Russia
    """
    url = "https://www.cbr-xml-daily.ru/latest.js"
    response = requests.get(url)

    for currency_code, rate in response.json()["rates"].items():
        currency_rate, created = CurrencyRate.objects.get_or_create(
            currency_code=currency_code
        )
        currency_rate.rate = Decimal(rate)
        currency_rate.save()
