from django.urls import path
from .views import get_dividends_summary

urlpatterns = [
    path('dividends-summary/', get_dividends_summary, name='dividends-summary'),
]
