from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView, name='Home'),
    path('getvalues/', views.GetValues, name='getvalues'),
    path('success/', views.SuccessView.as_view(), name='success'),
]