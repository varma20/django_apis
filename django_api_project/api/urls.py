from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("calculator/", calculator, name="calculator"),
    path("index.html/",index_view,name = "indexView")
]