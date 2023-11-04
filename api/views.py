from django.shortcuts import render
from .serializers import BookModelSerializer, ArticleModelSerializer, AppointmentTypeModelSerializer, RoleModelSerializer, Pay_MethodModelSerializer, User_infoModelSerializer, Social_mediaModelSerializer, Phone_numberModelSerializer, TagModelSerializer, WriterModelSerializer, SlotModelSerializer, PaymentModelSerializer,Phone_numberModelPostPutSerializer,Social_mediaModelPostPutSerializer, SlotModelPostPutSerializer, AppointmentPostPutSerializer, Pay_ReferencePostPutModelSerializer,AppointmentModelSerializer
from rest_framework import viewsets, status, generics, mixins
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Book, Article, Appointment_type, Role, Pay_method, User_Info, Social_media, Phone_number, Tag, Slot, Writer, Payment, Appointment
from .utils import filter_results_depending_on_role

class BookList(generics.ListAPIView):# PUBLIC
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

class BookInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):#public
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

class ArticleList(generics.ListAPIView):# public
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

class ArticleInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):#public
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
   
    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

class AppointmentTypeList(generics.ListAPIView):#public
    queryset = Appointment_type.objects.all()
    serializer_class = AppointmentTypeModelSerializer

class AppointmentTypeInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):#public
    queryset = Appointment_type.objects.all()
    serializer_class = AppointmentTypeModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)
    
class RoleList(generics.ListAPIView):#restricted
    queryset = Role.objects.all()
    serializer_class = RoleModelSerializer
    permission_classes = [IsAuthenticated]

class Pay_methodList(generics.ListAPIView):    #public
    queryset = Pay_method.objects.all()
    serializer_class = Pay_MethodModelSerializer
    
class User_InfoList(generics.ListAPIView):# restricted
    queryset = User_Info.objects.all()
    serializer_class = User_infoModelSerializer
    permission_classes = [IsAuthenticated]
    # follow 
    def get_queryset(self):
       
        def admin_action(user_info):
            return User_Info.objects.all()

        def client_action(user_info):
            return User_Info.objects.filter(role=3)
        
        def psico_action(user_info):
            return User_Info.objects.exclude(role=2)

        return filter_results_depending_on_role(self.request.headers, admin_action=admin_action, client_action=client_action, psico_action=psico_action)


class User_InfoInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):# restricted
    queryset = User_Info.objects.all()
    serializer_class = User_infoModelSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)
    
class Social_mediaList(generics.ListAPIView): # public
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaModelSerializer
    permission_classes = [IsAuthenticated]

class Social_mediaInstance(mixins.CreateModelMixin, generics.GenericAPIView): # restricted
    queryset = Appointment_type.objects.all()
    serializer_class = AppointmentTypeModelSerializer
    
    permission_classes = [IsAuthenticated]

    def post(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

class Phone_numberList(generics.ListAPIView): # public
    queryset = Phone_number.objects.all()
    serializer_class = Phone_numberModelSerializer
    permission_classes = [IsAuthenticated]

class Phone_numberInstance(APIView): # restricted
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = Phone_numberModelPostPutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
          
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Phone_numberInstanceDeletePut(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView): # restricted
    queryset = Phone_number.objects.all()
    serializer_class = Phone_numberModelPostPutSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class Social_mediaInstance(APIView): #restricted
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = Social_mediaModelPostPutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Social_mediaInstanceDeletePut(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):# restricted
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaModelPostPutSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class SlotInstance(APIView):#restricted
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = SlotModelPostPutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SlotInstance_PutPost(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):# restricted
    queryset = Slot.objects.all()
    serializer_class = SlotModelPostPutSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kargs):
        return self.destroy(request, *args, **kargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class TagList(generics.ListAPIView):# public
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer

class WriterList(generics.ListAPIView):# public
    queryset = Writer.objects.all()
    serializer_class = WriterModelSerializer

class WriterInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):# public
    queryset = Writer.objects.all()
    serializer_class = WriterModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)
    
class SlotList(generics.ListAPIView): # should filter by date, avalability , and owner, public
    serializer_class = SlotModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
       
        def admin_action(user_info):
            return Slot.objects.all()

        def client_action(user_info):
            return Slot.objects.filter(available=True)
        
        def psico_action(user_info):
            return Slot.objects.filter(owner=user_info)

        return filter_results_depending_on_role(self.request.headers, admin_action=admin_action, client_action=client_action, psico_action=psico_action)


class PaymentList(generics.ListAPIView): # should filter by date, owner and some filters more
    serializer_class = PaymentModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
       
        def admin_action(user_info):
            return Payment.objects.all()

        def client_action(user_info):
            # return all the payment of the certain client
            return Payment.objects.filter(owner=user_info.id)
        
        def psico_action(user_info):
            # has not permission
            return Payment.objects.none()

        return filter_results_depending_on_role(self.request.headers, admin_action=admin_action, client_action=client_action, psico_action=psico_action)

class PayInstance(mixins.RetrieveModelMixin, generics.GenericAPIView): # restricted
    permission_classes = [IsAuthenticated]    
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

class PaymentInstance(APIView): # this should be protected
    permission_classes = [IsAuthenticated]
    
    def post(self, request,format=None):
        serializer = Pay_ReferencePostPutModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentInstance_PutPost(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView): # restricted
    queryset = Payment.objects.all()
    serializer_class = Pay_ReferencePostPutModelSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kargs):
        return self.destroy(request, *args, **kargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class AppointmentInstance(APIView): # restricted
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = AppointmentPostPutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentInstance_PutPost(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView): # restricted
    queryset = Appointment.objects.all()
    serializer_class = AppointmentPostPutSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kargs):
        return self.destroy(request, *args, **kargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class AppointmentList(generics.ListAPIView): # should filter by date, owner and some filters more
    serializer_class = AppointmentModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
       
        def admin_action(user_info):
            return Appointment.objects.all()

        def client_action(user_info):
            return Appointment.objects.filter(client=user_info)
        
        def psico_action(user_info):
            return Appointment.objects.filter(host=user_info)

        return filter_results_depending_on_role(self.request.headers, admin_action=admin_action, client_action=client_action, psico_action=psico_action)


