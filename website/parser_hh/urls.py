from django.urls import path
from parser_hh import views

app_name = 'parser'

urlpatterns = [
    path('contacts/', views.contact, name='contacts'),
    path('', views.ParamsListView.as_view(), name='index'),
    path('delete-params', views.ParamsDeleteView.as_view(),
         name='delete-params'),
    path('create-options', views.create_params, name='create-options'),
    # path('create-options', views.CreateNewParams.as_view(),
    #      name='create-options'),
    path('delete-params/<int:pk>/', views.ParamsDeleteView.as_view(),
         name='delete-params'),
    path('delete-vacancy/<int:pk>/', views.VacancyDeleteView.as_view(),
         name='delete-vacancy'),
    path('results', views.VacancyListView.as_view(), name='results'),
    path('vacancy/<int:pk>/', views.VacancyDetailView.as_view(),
         name='vacancy')
]
