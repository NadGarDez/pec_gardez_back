from django.shortcuts import render
from .serializers import BookModelSerializer, ArticleModelSerializer, AppointmentTypeModelSerializer, RoleModelSerializer, Pay_MethodModelSerializer, User_infoModelSerializer, Social_mediaModelSerializer, Phone_numberModelSerializer, TagModelSerializer, WriterModelSerializer, SlotModelSerializer, PaymentModelSerializer,Phone_numberModelPostPutSerializer,Social_mediaModelPostPutSerializer
from rest_framework import viewsets, status, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
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
        return self.retrieve(self, request,*args, **kwargs)
    
class Social_mediaList(generics.ListAPIView): # shold list filtering by the owner 
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaModelSerializer

class Social_mediaInstance(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Appointment_type.objects.all()
    serializer_class = AppointmentTypeModelSerializer

    def post(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

class Phone_numberList(generics.ListAPIView): # should filter by the owner
    queryset = Phone_number.objects.all()
    serializer_class = Phone_numberModelSerializer

class Phone_numberInstance(APIView):
    def post(self, request, format=None):
        serializer = Phone_numberModelPostPutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
          
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Social_mediaInstance(APIView):
    def post(self, request, format=None):
        serializer = Social_mediaModelPostPutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer

class TagInstance(APIView): # this is only a practice

    def post(self, request, format=None):
        serializer = TagModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WriterList(generics.ListAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterModelSerializer

class WriterInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)
    
class SlotList(generics.ListAPIView): # should filter by date, avalability , and owner
    queryset = Slot.objects.all()
    serializer_class = SlotModelSerializer

class PaymentList(generics.ListAPIView): # should filter by date, owner and some filters more
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer

class PayInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)





# in the next practice we are going to use the relationships tool in django rest framework to serialize model relationship fields.
