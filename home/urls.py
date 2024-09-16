from django.contrib import admin
from django.urls import path, include # allauth
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
     
]
