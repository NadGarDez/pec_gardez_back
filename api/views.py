from django.shortcuts import render
from .serializers import BookModelSerializer, ArticleModelSerializer, AppointmentTypeModelSerializer, RoleModelSerializer, Pay_MethodModelSerializer, User_infoModelSerializer, Social_mediaModelSerializer, Phone_numberModelSerializer, TagModelSerializer, WriterModelSerializer, SlotModelSerializer, PaymentModelSerializer
from rest_framework import viewsets, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Book, Article, Appointment_type, Role, Pay_method, User_Info, Social_media, Phone_number, Tag, Slot, Writer, Payment


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    
class BookInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

    
class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class ArticleInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
   
    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)


class AppointmentTypeList(generics.ListAPIView):
    queryset = Appointment_type.objects.all()
    serializer_class = AppointmentTypeModelSerializer


class AppointmentTypeInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Appointment_type.objects.all()
    serializer_class = AppointmentTypeModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)
    
class RoleList(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleModelSerializer

class Pay_methodList(generics.ListAPIView):    
    queryset = Pay_method.objects.all()
    serializer_class = Pay_MethodModelSerializer

class User_InfoList(generics.ListAPIView):
    queryset = User_Info.objects.all()
    serializer_class = User_infoModelSerializer

class User_InfoInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = User_Info.objects.all()
    serializer_class = User_infoModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrive(self, request,*args, **kwargs)
    
class Social_mediaList(generics.ListAPIView): # shold list filtering by the owner 
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaModelSerializer

class Phone_numberList(generics.ListAPIView): # should filter by the owner
    queryset = Phone_number.objects.all()
    serializer_class = Phone_numberModelSerializer

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer

class WriterList(generics.ListAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterModelSerializer

class WriterInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrive(self, request,*args, **kwargs)
    
class SlotList(generics.ListAPIView): # should filter by date, avalability , and owner
    queryset = Slot.objects.all()
    serializer_class = SlotModelSerializer

class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer

class PayInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrive(self, request,*args, **kwargs)





# in the next practice we are going to use the relationships tool in django rest framework to serialize model relationship fields.
