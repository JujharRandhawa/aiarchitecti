"""
URL configuration for aiarchitect_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from main.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
