from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_landing_page, name = 'landing_page'),
    path('home/', views.homepage, name = 'home')
]
