from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path("books/", views.BookList),
    path("book/<int:pk>", views.BookInstance),
    path("articles/", views.ArticleList),
    path("article/<int:pk>", views.ArticleInstance),
    path("appointment_types/", views.appointmentTypeList),
    path("appointment_type/<int:pk>", views.AppointmentTypeInstance)
]