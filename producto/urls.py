# Estas son las url a utilziar para mi aplicación de productp

from django.contrib import admin

from django.urls import path
from producto import views

urlpatterns = [
    path('Hola mundo', views.hola_mundo),
    path('',views.inicio)
]