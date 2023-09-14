from rest_framework import views, status
from rest_framework.response import Response
from converter.models import CurrencyRate
from converter.serializers import CurrencyRateSerializer


class CurrencyConversionView(views.APIView):
    def get(self, request):
        from_currency = request.query_params.get('from')
        to_currency = request.query_params.get('to')
        value = float(request.query_params.get('value', 1))

        try:
            from_rate = CurrencyRate.objects.get(currency_code=from_currency)
            to_rate = CurrencyRate.objects.get(currency_code=to_currency)
        except CurrencyRate.DoesNotExist:
            return Response({"error": "Invalid currency code"}, status=status.HTTP_400_BAD_REQUEST)

        converted_value = (value * to_rate.rate) / from_rate.rate

        response_data = {
            "result": round(converted_value, 2)
        }

        return Response(response_data, status=status.HTTP_200_OK)
