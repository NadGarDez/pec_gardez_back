from django.shortcuts import render
from .serializers import BookModelSerializer, ArticleModelSerializer, AppointmentTypeModelSerializer
from rest_framework import viewsets, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Book, Article, Appointment_type


@api_view(['GET'])
def BookList_func(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many = True)
        return Response(data = serializer.data)

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    
@api_view(['GET'])
def BookInstance_function(request, pk):
    if request.method == 'GET':
        try:
            book = Book.objects.get(pk = pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookModelSerializer(book)
        return Response(serializer.data)
    
class BookInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

@api_view(['GET'])
def ArticleList_function(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many = True)
        return Response(data = serializer.data)
    
class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


@api_view(['GET'])    
def ArticleInstance_function(request, pk):
    if request.method == 'GET':
        try:
            book = Article.objects.get(pk = pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ArticleModelSerializer(book)
        return Response(serializer.data)

class ArticleInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
   
    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

    
@api_view(['GET'])
def appointmentTypeList_funciton(request):
    if request.method == 'GET':
        types = Appointment_type.objects.all()
        serializer = AppointmentTypeModelSerializer(types, many = True)
        return Response(data = serializer.data)

class AppointmentTypeList(generics.ListAPIView):
    queryset = Appointment_type.objects.all()
    serializer_class = AppointmentTypeModelSerializer


@api_view(['GET'])
def AppointmentTypeInstance_function(request, pk):
    if request.method == 'GET':
        try:
            type = Appointment_type.objects.get(pk = pk)
        except Appointment_type.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AppointmentTypeModelSerializer(type)
        return Response(serializer.data)

class AppointmentTypeInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Appointment_type.objects.all()
    serializer_class = AppointmentTypeModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)
    


@api_view(['get'])
def index1(request, format=None):
    return Response({
        'books':reverse('books', request=request,format=format),
        'articles':reverse('articles', request=request, format=format)
    })



# in the next practice we are going to use the relationships tool in django rest framework to serialize model relationship fields.
