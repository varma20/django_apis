from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signin/',index_view,name='User Sign In'),
    path('create/',create_user,name="Create User"),
    path('details/',get_details,name="User Details")
]