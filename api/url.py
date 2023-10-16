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
    path("appointment/", views.AppointmentInstance.as_view(), name="appointment"),
    path("appointment/<int:pk>", views.AppointmentInstance_PutPost.as_view(), name="appointment_put_post"),
    path("appointments/", views.AppointmentList.as_view(), name="appointments"),
    path("roles/", views.RoleList.as_view(), name="roles"),
    path("slots/", views.SlotList.as_view(), name="slots"),
    path("slot/", views.SlotInstance.as_view(), name='slot'),
    path("slot/<int:pk>", views.SlotInstance_PutPost.as_view(), name='slot_put_post'),
    path("pay_methods/", views.Pay_methodList.as_view(), name="pay_methods"),
    path("users/",views.User_InfoList.as_view(), name="users" ), # this should be parcialy locked
    path("user/<int:pk>", views.User_InfoInstance.as_view(), name="user"),
    path("social_media_list/", views.Social_mediaList.as_view(), name="social_media_list"), # should filter by owner
    path("social_media/",views.Social_mediaInstance.as_view(), name="social_media"),
    path("social_media/<int:pk>",views.Social_mediaInstanceDeletePut.as_view(), name="social_media_put_post"),
    path("phone_numbers/", views.Phone_numberList.as_view(), name="phone_numbers"), # should filter by owner,
    path("phone/", views.Phone_numberInstance.as_view(), name="phone"),
    path("phone/<int:pk>", views.Phone_numberInstanceDeletePut.as_view(), name="phone_put_delete"),
    path("tag/", views.TagInstance.as_view(), name="tag "), 
    path("tags/", views.TagList.as_view(), name="tags"), # it's probably this endpoint be unused
    path("writers/", views.WriterList.as_view(), name="writers"),
    path("writer/<int:pk>", views.WriterInstance.as_view(),name="writer"),
    path("payments/", views.PaymentList.as_view(), name="payments"),
    path("payment/<int:pk>", views.AppointmentInstance_PutPost.as_view(),  name="payment_put_post"),
    path("payment_put_post/<int:pk>", views.PaymentInstance_PutPost.as_view(),  name="payment"),
    path("payment/", views.PaymentInstance.as_view(), name='payment_post')
]