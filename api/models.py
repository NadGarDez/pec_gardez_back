from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Writer(models.Model): # listo el serializer
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    internal_writer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
       
        if len(self.first_name)<1:
            return self.internal_writer.get_username()
        else:
            return self.first_name

class Tag(models.Model): #listo el serializer
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=50)
    def __str__(self):
        return self.tag_name

class Article(models.Model): # listo el serializer
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, default="The Article title")
    tags = models.ManyToManyField(Tag)
    writers = models.ManyToManyField(Writer)
    principal_image = models.URLField(max_length=255)
    content = models.TextField(default="An article")
    def __str__(self):
        return self.title

class Book(models.Model): # listo el serializer
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, default="The Book title")
    tags = models.ManyToManyField(Tag)
    writers = models.ManyToManyField(Writer)
    principal_image = models.URLField(max_length=255)
    resume=models.TextField(default="Default text")
    download_url = models.URLField(max_length=255)
    def __str__(self):
        return self.title

class Appointment_type(models.Model): # listo el serializer
    options =[
        ("usd", "USD (US Dollar)"),
        ("eur", "EUR (Euro)"),
        ("ved","VED (Bolivar)")
    ]
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    currency = models.CharField(choices=options, max_length=15)
    def __str__(self):
        return self.product_name

class Pay_method(models.Model): # listo el serializer
    id = models.AutoField(primary_key=True)
    method_name = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    bank_code = models.CharField(max_length=50)
    owner_identification = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=100)
    def __str__(self):
        return "Pay method: "+ self.method_name


class Payment(models.Model): # listo el serializer
    id = models.AutoField(primary_key=True)
    method = models.ForeignKey(Pay_method,on_delete=models.CASCADE)
    transaction_code = models.CharField(max_length=255)
    product =  models.ForeignKey(Appointment_type,on_delete=models.CASCADE)
    def __str__(self):
        return "Payment: " + id

class Role(models.Model): # listo el serializer
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50)
    def __str__(self):
        return self.role_name


class User_Info(models.Model): # listo el serializer
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_image = models.URLField(max_length=255)
    resume = models.TextField()
    time_zone = models.CharField(max_length=10)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name

class Social_media(models.Model): # listo serializer
    id = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User_Info, on_delete=models.CASCADE)
    url = models.URLField(max_length=255)
    def __str__(self):
        return self.user_name

class Phone_number(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20)
    country_code = models.CharField(max_length=10)
    owner = models.ForeignKey(User_Info, on_delete=models.CASCADE, related_name='owner')
    def __str__(self):
        return self.phone_number

class Slot(models.Model): # listo el serializer
    id = models.AutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    time_in_minutes = models.IntegerField()
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User_Info, on_delete=models.CASCADE, related_name='slot_owner')
    def __str__(self):
        return "Slot " +  str(self.id)
    
class Appointment(models.Model): # listo el serializer
    id = models.AutoField(primary_key=True)
    host = models.ForeignKey(User_Info,on_delete=models.CASCADE, related_name="host_user")
    client = models.ForeignKey(User_Info,on_delete=models.CASCADE, related_name="client_user")
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE)
    pay_reference = models.OneToOneField(Payment, on_delete=models.CASCADE, blank=True, null=True)
    meet_url = models.URLField(max_length=255)
    appointment_type = models.ForeignKey(Appointment_type,on_delete=models.CASCADE)
    def __str__(self):
        return "Appointment: " + str(self.id)