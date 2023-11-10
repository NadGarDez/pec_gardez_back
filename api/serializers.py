from rest_framework import serializers

from .models import Book, Article,Appointment_type, Writer, Tag, Writer, Role, Slot, Pay_method, Payment, Appointment, User_Info, Social_media, Phone_number
from django.contrib.auth.models import User


class Pay_MethodModelSerializer(serializers.HyperlinkedModelSerializer):# listo el view
    class Meta:
        model = Pay_method
        fields = ['id','method_name','bank_name','bank_code','owner_identification','owner_name']


class RoleModelSerializer(serializers.HyperlinkedModelSerializer): # listo el view
    class Meta:
        model = Role
        fields = ['role_name', 'id']

class SlotModelSerializer(serializers.HyperlinkedModelSerializer):# listo el view
    class Meta:
        model = Slot
        fields = ['id','start_date', 'end_date', 'time_in_minutes', 'available']

class WriterModelSerializer(serializers.HyperlinkedModelSerializer): # listo el view
    class Meta:
        model = Writer
        fields = ['first_name', 'last_name', 'id']

class TagModelSerializer(serializers.HyperlinkedModelSerializer): # listo el view
    class Meta:
        model = Tag
        fields = ['tag_name', 'id']

class BookModelSerializer(serializers.HyperlinkedModelSerializer): #listo el view
    writers = WriterModelSerializer(many=True)
    tags = TagModelSerializer(many=True)
    class Meta:
        model = Book
        fields= ['id','title', 'principal_image', 'download_url', 'resume', 'writers', 'tags']

class ArticleModelSerializer(serializers.HyperlinkedModelSerializer):# listo el view
    writers = WriterModelSerializer(many=True)
    tags = TagModelSerializer(many=True)
    class Meta:
        model = Article
        fields = ['id', 'title', 'principal_image', 'content', 'writers', 'tags']

class AppointmentTypeModelSerializer(serializers.HyperlinkedModelSerializer): # listo el view
    class Meta:
        model = Appointment_type
        fields = ['id','product_name', 'description', 'price', 'currency']

class Pay_ReferencePostPutModelSerializer(serializers.HyperlinkedModelSerializer):
    method = serializers.PrimaryKeyRelatedField(queryset=Pay_method.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Appointment_type.objects.all())
    owner =  serializers.PrimaryKeyRelatedField(queryset=User_Info.objects.all())
    class Meta:
        model = Payment
        fields = ['method', 'transaction_code', 'product', 'owner']


class PaymentModelSerializer(serializers.HyperlinkedModelSerializer): # listo el view
    method = Pay_MethodModelSerializer()
    product = AppointmentTypeModelSerializer()
    owner = serializers.PrimaryKeyRelatedField(queryset=User_Info.objects.all())
    
    class Meta:
        model = Payment
        fields = ['id','method','transaction_code','product', 'owner']

class UserSerializer(serializers.HyperlinkedModelSerializer): # doesn't need view
    class Meta:
        model = User
        fields = ['username']

class User_infoModelSerializer(serializers.HyperlinkedModelSerializer): # listo el serialzer
    
    user = UserSerializer()
    role = RoleModelSerializer()

    class Meta:
        model = User_Info
        fields = ['id','user','first_name','last_name','user_image','resume','time_zone','role']

class AppointmentModelSerializer(serializers.HyperlinkedModelSerializer): # listo el view
    client = User_infoModelSerializer()
    host = User_infoModelSerializer()
    slot = SlotModelSerializer()
    pay_reference = PaymentModelSerializer()
    appointment_type = AppointmentTypeModelSerializer()

    class Meta:
        model = Appointment
        fields = ['id','host','client','slot','pay_reference','meet_url','appointment_type']

class Social_mediaModelSerializer(serializers.HyperlinkedModelSerializer): # listo el view
    owner = User_infoModelSerializer()

    class Meta:
        model = Social_media 
        fields = ['id','platform','user_name','owner','url']

class Phone_numberModelSerializer(serializers.HyperlinkedModelSerializer): # listo el view
    owner = User_infoModelSerializer()

    class Meta:
        model = Phone_number
        fields = ['id','phone_number','country_code','owner']

class Phone_numberModelPostPutSerializer(serializers.HyperlinkedModelSerializer): # listo el view
    owner = serializers.PrimaryKeyRelatedField(queryset=User_Info.objects.all())

    class Meta:
        model = Phone_number
        fields = ['phone_number','country_code', 'owner']

class Social_mediaModelPostPutSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User_Info.objects.all())
    class Meta:
        model = Social_media 
        fields = ['platform','user_name','owner','url']

class SlotModelPostPutSerializer(serializers.HyperlinkedModelSerializer):     
    owner = serializers.PrimaryKeyRelatedField(queryset=User_Info.objects.all())
    class Meta:
        model = Slot
        fields = ['start_date', 'end_date', 'time_in_minutes', 'available', 'owner']
    
class AppointmentPostPutSerializer(serializers.HyperlinkedModelSerializer):
    client =  serializers.PrimaryKeyRelatedField(queryset=User_Info.objects.all()) 
    host = serializers.PrimaryKeyRelatedField(queryset=User_Info.objects.all()) 
    slot =  serializers.PrimaryKeyRelatedField(queryset=Slot.objects.all()) 
    pay_reference = serializers.PrimaryKeyRelatedField(queryset=Payment.objects.all()) 
    appointment_type = serializers.PrimaryKeyRelatedField(queryset=Appointment_type.objects.all()) 

    class Meta:
        model = Appointment
        fields = ['host','client','slot','pay_reference','meet_url','appointment_type']


# http POST http://localhost:8000/api/appointment/ host=3 client=1 slot=1 meet_url=https://www.google.com appointment_type=1