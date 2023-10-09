from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path("books/", views.BookList.as_view(), name="books"),
    path("book/<int:pk>", views.BookInstance.as_view()),
    path("articles/", views.ArticleList.as_view(), name="articles"),
    path("article/<int:pk>", views.ArticleInstance.as_view()),
    path("appointment_types/", views.AppointmentTypeList.as_view()),
    path("appointment_type/<int:pk>", views.AppointmentTypeInstance.as_view()),
    path("roles/", views.RoleList.as_view(), name="roles"),
    path("slots/", views.SlotList.as_view(), name="slots"),
    path("pay_methods/", views.Pay_methodList.as_view(), name="pay_methods"),
    path("users/",views.User_InfoList.as_view(), name="users" ), # this should be parcialy locked
    path("user/<int:pk>", views.User_InfoInstance.as_view(), name="user"),
    path("social_media/", views.Social_mediaList.as_view(), name="social_media"), # should filter by owner
    path("phone_numbers/", views.Phone_numberList.as_view(), name="phone_numbers"), # should filter by owner
    path("tags/", views.TagList.as_view(), name="tags"), # it's probably this endpoint be unused
    path("writers/", views.WriterList.as_view(), name="writers"),
    path("writer/<int:pk>", views.WriterInstance.as_view(),name="writer"),
    path("payments/", views.PaymentList.as_view(), name="payments"),
    path("payment/<int:pk>", views.PayInstance.as_view(),  name="payment")
]