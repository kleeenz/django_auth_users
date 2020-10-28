from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('accounts/login/sign_up/', views.sign_up, name = 'sign_up'),
    path('log_out/', views.log_out, name = 'log_out')
]