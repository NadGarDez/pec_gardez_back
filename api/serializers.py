from rest_framework import serializers

from .models import Book, Article,Appointment_type

class BookModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields= ['id','title', 'principal_image', 'download_url', 'resume']

class ArticleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'principal_image', 'content']

class AppointmentTypeModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment_type
        fields = ['id','product_name', 'description', 'price', 'currency']