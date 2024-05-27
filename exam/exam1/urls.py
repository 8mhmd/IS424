from django.urls import path
from . import views

app_name = "exam1"

urlpatterns = [
    path("", views.index, name="index"),
    path("part3/", views.part3, name="part3"),
    path("part1/", views.part1, name="part1"),
    path("part4/", views.part4, name="part4")
    ]