from django.contrib import admin
from django.urls import path, include
from prediction import views

urlpatterns = [
    path("", views.index, name="home")
]