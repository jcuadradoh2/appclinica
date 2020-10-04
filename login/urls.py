from django.contrib import admin
from django.urls import path
from login.views import LoginView
from django.conf import settings
app_name = "login"
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]