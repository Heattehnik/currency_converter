from _decimal import Decimal
import requests
from converter.models import CurrencyRate


def get_currencies():
    url = 'https://www.cbr-xml-daily.ru/latest.js'
    response = requests.get(url)

    for currency_code, rate in response.json()['rates'].items():
        currency_rate, created = CurrencyRate.objects.get_or_create(currency_code=currency_code)
        currency_rate.rate = Decimal(rate)
        currency_rate.save()


if __name__ == '__main__':
    get_currencies()
