from django.urls import path, re_path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    # main view - full dashboard 
    path('index/', views.IndexView.as_view(), name='index'),
    path('index/get_stock_data/', views.getStockData),
    path('index/get_covid_data/', views.getCovidData),
    path('index/get_employment_data/', views.getEmploymentData),
    path('index/get_finance_data/', views.getFinanceData),
    path('index/get_corperation_data/', views.getCorperationData),
    path('index/get_prealert_data/', views.getPreAlertData),
    path('info/', views.InfoView.as_view(), name='info'),
    path('team/', views.TeamView.as_view(), name='team'),
    path('data/', views.getCSVData, name='data')

]