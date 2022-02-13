from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('uslugi/', views.uslugi, name="uslugi"),
    path('contacts/', views.contacts, name="contacts"),
]
