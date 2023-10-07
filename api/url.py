from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path("", views.index1),
    path("books/", views.BookList.as_view(), name="books"),
    path("book/<int:pk>", views.BookInstance.as_view()),
    path("articles/", views.ArticleList.as_view(), name="articles"),
    path("article/<int:pk>", views.ArticleInstance.as_view()),
    path("appointment_types/", views.AppointmentTypeList.as_view()),
    path("appointment_type/<int:pk>", views.AppointmentTypeInstance.as_view())
]