from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView,CreateView, UpdateView

from dashboard.module import stock, covid, employment, finance, pre_alert, corperation, csv_read, liabiity_roe

import json

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['finance_list'] = ['ROE', '부채비율', '매출액증가율', '총자산회전율']
        context['locale_list'] = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '세종', '울산', '인천', '전남', '전북', '제주', '충남', '충북']
        context['sector_list'] = ['건설업', '공공행정, 국방 및 사회보장 행정', '광업', '교육 서비스업', '금융 및 보험업', '농업, 임업 및 어업', '도매 및 소매업', '보건업 및 사회복지 서비스업', '부동산업', '사업시설 관리, 사업 지원 및 임대 서비스업', '수도, 하수 및 폐기물 처리, 원료 재생업', '숙박 및 음식점업', '예술, 스포츠 및 여가관련 서비스업', '운수 및 창고업', '전기, 가스, 증기 및 공기조절 공급업', '전문, 과학 및 기술 서비스업', '정보통신업', '제조업', '협회 및 단체, 수리 및 기타 개인 서비스업']
        return context

class InfoView(TemplateView):
    template_name = "info.html"

class TeamView(TemplateView):
    template_name = "team.html"

def getCSVData(request):
    keyword = request.GET.get('name')
    csv_dict = csv_read.readCSVData(keyword)
    return render(request, "dataset.html", csv_dict)


def getStockData(request):
    date = request.GET.get('date')
    keyword = request.GET.get('keyword')
    stock_data = stock.showStock(keyword,int(date))
    return HttpResponse(stock_data, content_type='application/json')


def getCovidData(request):
    period = request.GET.get('period')
    covid_data = covid.showCovid(int(period))
    return HttpResponse(json.dumps(covid_data), content_type='application/json')

def getEmploymentData(request):
    locale = request.GET.get('locale')
    year = request.GET.get('year')
    size = request.GET.get('size')

    employment_data = employment.showEmployment(locale, year, size)
    return HttpResponse(json.dumps(employment_data), content_type='application/json')

def getFinanceData(request):
    locale = request.GET.get('locale')
    sector = request.GET.get('sector')
    column = request.GET.get('column')

    finance_data = finance.showFinance(column, locale, sector)
    return HttpResponse(json.dumps(finance_data), content_type='application/json')

def getCorperationData(request):
    sector = request.GET.get('sector')
    year = request.GET.get('year')
    size = request.GET.get('size')

    corperation_data = corperation.showCorperation(year, sector, size)
    return HttpResponse(json.dumps(corperation_data), content_type='application/json')

def getPreAlertData(request):
    year = request.GET.get('year')
    size = request.GET.get('size')
    locale = request.GET.get('locale')
    sector = request.GET.get('sector')
    pre_alert_data = pre_alert.showPreAlert(year, locale, size, sector)
    return HttpResponse(json.dumps(pre_alert_data), content_type='application/json')

def getLiabilityAndROEData(request):
    year = request.GET.get('year')
    size = request.GET.get('size')
    locale = request.GET.get('locale')
    liability_roe_data = liabiity_roe.showLiabilityAndROE(year, locale, size)
    return HttpResponse(json.dumps(liability_roe_data), content_type='application/json')
