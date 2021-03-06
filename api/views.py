import os

from bittrex import *
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Wallet

API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']

API = Bittrex(API_KEY, API_SECRET, api_version=API_V2_0)  # or defaulting to v1.1 as Bittrex(None, None)


def index(request):
    response = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-neo')
    jdata = json.loads(response.content)
    context = jdata['result'][0]
    print(context['MarketName'])
    return render(request, 'api/index.html', context)


def test(request):
    context = API.get_balance('BTC')
    results = context['result']
    print(results)

    wallet = Wallet(currency=results['Currency'], balance=results['Balance'], available=results['Available'])
    wallet.save()
    return render(request, 'api/test.html', context['result'])



class ThatApiView(APIView):
    """
    Documentation goes here
    """
    def get(self, request, format=None):
        context = API.get_balance('BTC')
        results = context['result']
        return Response({'result': results})

