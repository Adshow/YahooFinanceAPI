from django.shortcuts import render
from django.http import JsonResponse
from .models import Dividend
from .services import load_dividends_to_db

def get_dividends_summary(request):
    symbol = request.GET.get('symbol')
    year = request.GET.get('year')
    
    if not symbol or not year:
        return JsonResponse({"error": "Both symbol and year parameters are required."}, status=400)
    
    # Chame a função load_dividends_to_db para carregar os dados antes de consultar
    load_dividends_to_db(symbol)
    
    dividends = Dividend.objects.filter(symbol=symbol, year=year)
        
    total_dividends = sum(dividend.amount for dividend in dividends)

    return JsonResponse({"symbol": symbol, "year": year, "total_dividends": total_dividends})
