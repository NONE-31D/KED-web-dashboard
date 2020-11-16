from django.urls import path, re_path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    # main view - full dashboard 
    path('index/', views.IndexView.as_view(), name='index'),
    path('index/get_stock_data/', views.getStockData),
    path('index/get_covid_data/', views.getCovidData)
]