from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view_with_post,name="Login View"),
    path('logout/',logout_view_with_post,name="Logout View"),
    path('login/home/',home_view,name="Home View")
]
