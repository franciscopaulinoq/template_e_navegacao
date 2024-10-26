# enquetes/urls.py
from django.urls import path
from . import views

app_name = 'enquetes'

urlpatterns = [
    path('', views.index, name='index'),
]