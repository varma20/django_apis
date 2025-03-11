from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signin/',user_sign_in,name='User Sign In')
]