from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('encoding/', views.encode_image, name = 'encode-img'),
    path('success/', views.success, name = 'success')
]