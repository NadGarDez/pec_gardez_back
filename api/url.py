from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path("books/", views.listBook),
    path("articles/", views.listArticles),
    path("appointment_types/", views.appointmentTypeList)
]