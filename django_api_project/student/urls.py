from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('create/',create_user,name = 'Create User'),
    path('delete/',delete_user_from_delete_request,name = "Delete User"),
    path('details/',user_details_from_get_request,name=" User Details")
]