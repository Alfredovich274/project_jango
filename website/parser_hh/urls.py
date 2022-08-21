from django.urls import path
from parser_hh import views

app_name = 'parser'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('contacts/', views.contact, name='contacts'),
    path('results/', views.results, name='results'),
    # path('vacancy/', views.vacancy, name='vacancy'),
]
