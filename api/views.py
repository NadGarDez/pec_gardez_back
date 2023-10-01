from django.shortcuts import render
from .serializers import BookModelSerializer, ArticleModelSerializer, AppointmentTypeModelSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Article, Appointment_type


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


@api_view(['GET'])
def BookList(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many = True)
        return Response(data = serializer.data)
    
@api_view(['GET'])
def BookInstance(request, pk):
    if request.method == 'GET':
        try:
            book = Book.objects.get(pk = pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookModelSerializer(book)
        return Response(serializer.data)

@api_view(['GET'])
def ArticleList(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many = True)
        return Response(data = serializer.data)


@api_view(['GET'])    
def ArticleInstance(request, pk):
    if request.method == 'GET':
        try:
            book = Article.objects.get(pk = pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ArticleModelSerializer(book)
        return Response(serializer.data)

    
@api_view(['GET'])
def appointmentTypeList(request):
    if request.method == 'GET':
        types = Appointment_type.objects.all()
        serializer = AppointmentTypeModelSerializer(types, many = True)
        return Response(data = serializer.data)
    

@api_view(['GET'])
def AppointmentTypeInstance(request, pk):
    if request.method == 'GET':
        try:
            type = Appointment_type.objects.get(pk = pk)
        except Appointment_type.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AppointmentTypeModelSerializer(type)
        return Response(serializer.data)

    