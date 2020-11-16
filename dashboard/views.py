from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView,CreateView, UpdateView

from dashboard.module import stock ,covid

import json

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


def getStockData(request):
    date = request.GET.get('date')
    keyword = request.GET.get('keyword')
    stock_data = stock.showStock(keyword,int(date))
    return HttpResponse(stock_data, content_type='application/json')


def getCovidData(request):
    period = request.GET.get('period')
    covid_data = covid.showCovid(int(period))
    return HttpResponse(json.dumps(covid_data), content_type='application/json')