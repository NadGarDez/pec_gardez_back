from rest_framework import serializers

from .models import Book, Article,Appointment_type, Writer

class BookModelSerializer(serializers.HyperlinkedModelSerializer):
    writers = serializers.PrimaryKeyRelatedField(many=True, queryset = Writer.objects.all())
    class Meta:
        model = Book
        fields= ['id','title', 'principal_image', 'download_url', 'resume', 'writers']

class ArticleModelSerializer(serializers.HyperlinkedModelSerializer):
    writers = serializers.PrimaryKeyRelatedField(many=True, queryset = Writer.objects.all())
    class Meta:
        model = Article
        fields = ['id', 'title', 'principal_image', 'content', 'writers']

class AppointmentTypeModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment_type
        fields = ['id','product_name', 'description', 'price', 'currency']