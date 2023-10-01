from django.contrib import admin
from .models import Writer, Book, Tag, Article, Slot, Appointment, Appointment_type, Pay_method, Payment, Role, Social_media, Phone_number, User_Info

# Register your models here.
admin.site.register([Writer, Book, Tag, Article, Slot, Appointment, Appointment_type, Pay_method, Payment, Role, Social_media, Phone_number, User_Info])