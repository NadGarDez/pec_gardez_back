from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import BookModelSerializer, ArticleModelSerializer, AppointmentTypeModelSerializer
from rest_framework import viewsets
from .models import Book, Article, Appointment_type


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

def listBook(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many = True)
        return JsonResponse(serializer.data, safe = False)

def listArticles(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many = True)
        return JsonResponse(serializer.data, safe=False)
    
def appointmentTypeList(request):
    if request.method == 'GET':
        types = Appointment_type.objects.all()
        serializer = AppointmentTypeModelSerializer(types, many = True)
        return JsonResponse(serializer.data, safe=False)
    