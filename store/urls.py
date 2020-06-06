from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_pg, name='home_pg')
]