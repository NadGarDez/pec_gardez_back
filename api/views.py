from django.shortcuts import render
from .serializers import BookModelSerializer, ArticleModelSerializer, AppointmentTypeModelSerializer, RoleModelSerializer, Pay_MethodModelSerializer, User_infoModelSerializer, Social_mediaModelSerializer, Phone_numberModelSerializer, TagModelSerializer, WriterModelSerializer, SlotModelSerializer, PaymentModelSerializer,Phone_numberModelPostPutSerializer,Social_mediaModelPostPutSerializer, SlotModelPostPutSerializer, AppointmentPostPutSerializer, Pay_ReferencePostPutModelSerializer,AppointmentModelSerializer
from rest_framework import viewsets, status, generics, mixins
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Book, Article, Appointment_type, Role, Pay_method, User_Info, Social_media, Phone_number, Tag, Slot, Writer, Payment, Appointment
from .utils import filter_results_depending_on_role, get_user_id_from_token, get_token_from_headers, get_user_info_from_user_id,get_user_info_from_headers

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
    
class RoleList(generics.ListAPIView):# this view may be deleted
    queryset = Role.objects.all()
    serializer_class = RoleModelSerializer
    permission_classes = [IsAuthenticated]

class Pay_methodList(generics.ListAPIView):    #public
    queryset = Pay_method.objects.all()
    serializer_class = Pay_MethodModelSerializer
    
class User_InfoList(generics.ListAPIView):# restricted
    serializer_class = User_infoModelSerializer
    permission_classes = [IsAuthenticated]

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

    def is_owner_or_admin(model_instance, user_info):
        return model_instance.id == user_info.id or user_info.role.role_name == 'admin'

    def get(self, request, pk, *args, **kwargs): # required permission
        user_info = get_user_info_from_headers(request)
        model_instance = User_Info.objects.get(id=pk)

        if self.is_owner_or_admin(model_instance, user_info):
            return self.destroy(request, *args, **kargs)
        else:
            return Response("You cannot read this item", status=status.HTTP_400_BAD_REQUEST)
        return self.retrieve(self, request,*args, **kwargs)
    
class Social_mediaList(generics.ListAPIView): # public
    serializer_class = Social_mediaModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
       
        def admin_action(user_info):
            return Social_media.objects.all()

        def client_action(user_info):
            return Social_media.objects.filter(owner=user_info)
        
        def psico_action(user_info):
            return Social_media.objects.filter(owner=user_info)

        return filter_results_depending_on_role(self.request.headers, admin_action=admin_action, client_action=client_action, psico_action=psico_action)


class Social_mediaInstance(mixins.CreateModelMixin, generics.GenericAPIView): # restricted
    queryset = Appointment_type.objects.all()
    serializer_class = AppointmentTypeModelSerializer
    
    permission_classes = [IsAuthenticated]

    def post(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

class Phone_numberList(generics.ListAPIView): # public
    serializer_class = Phone_numberModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
       
        def admin_action(user_info):
            return Phone_number.objects.all()

        def client_action(user_info):
            return Phone_number.objects.filter(owner=user_info)
        
        def psico_action(user_info):
            return Phone_number.objects.filter(owner=user_info)

        return filter_results_depending_on_role(self.request.headers, admin_action=admin_action, client_action=client_action, psico_action=psico_action)


class Phone_numberInstance(APIView): # restricted
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None): # needed permission
        serializer = Phone_numberModelPostPutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
          
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Phone_numberInstanceDeletePut(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView): # restricted
    queryset = Phone_number.objects.all()
    serializer_class = Phone_numberModelPostPutSerializer
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(model_instance, user_info):
        return model_instance.owner.id == user_info.id or user_info.role.role_name == 'admin'

    def delete(self, request,pk, *args, **kargs): # needed permission
        user_info = get_user_info_from_headers(request)
        phone_number = Phone_number.objects.get(id=pk)

        if self.is_owner_or_admin(phone_number, user_info):
            return self.destroy(request, *args, **kargs)
        else:
            return Response("You cannot delete this item", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):# needed permission
        user_info = get_user_info_from_headers(request)
        phone_number = Phone_number.objects.get(id=pk)

        if self.is_owner_or_admin(phone_number, user_info):
            return self.update(request, *args, **kargs)
        else:
            return Response("You cannot update this item", status=status.HTTP_400_BAD_REQUEST)

class Social_mediaInstance(APIView): #restricted
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None): # needed permission
        serializer = Social_mediaModelPostPutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Social_mediaInstanceDeletePut(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):# restricted
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaModelPostPutSerializer
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(model_instance, user_info):
        return model_instance.owner.id == user_info.id or user_info.role.role_name == 'admin'

    def delete(self, request,pk, *args, **kargs): # needed permission
        user_info = get_user_info_from_headers(request)
        social_media_instance = Social_media.objects.get(id=pk)

        if self.is_owner_or_admin(social_media_instance, user_info):
            return self.destroy(request, *args, **kargs)
        else:
            return Response("You cannot delete this item", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):# needed permission
        user_info = get_user_info_from_headers(request)
        social_media_instance = Social_media.objects.get(id=pk)

        if self.is_owner_or_admin(social_media_instance, user_info):
            return self.update(request, *args, **kargs)
        else:
            return Response("You cannot update this item", status=status.HTTP_400_BAD_REQUEST)
class SlotInstance(APIView):#restricted
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None): # needed permission
        serializer = SlotModelPostPutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SlotInstance_PutPost(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):# restricted
    queryset = Slot.objects.all()
    serializer_class = SlotModelPostPutSerializer
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(model_instance, user_info):
        return model_instance.owner.id == user_info.id or user_info.role.role_name == 'admin'

    def delete(self, request,pk, *args, **kargs): # needed permission
        user_info = get_user_info_from_headers(request)
        slot = Slot.objects.get(id=pk)

        if self.is_owner_or_admin(slot, user_info):
            return self.destroy(request, *args, **kargs)
        else:
            return Response("You cannot delete this item", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):# needed permission
        user_info = get_user_info_from_headers(request)
        slot = Social_media.objects.get(id=pk)

        if self.is_owner_or_admin(slot, user_info):
            return self.update(request, *args, **kargs)
        else:
            return Response("You cannot update this item", status=status.HTTP_400_BAD_REQUEST)

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

class PaymentInstance(APIView): # this should be protected
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentModelSerializer

    
    def post(self, request,format=None): # needed permission
        serializer = Pay_ReferencePostPutModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PaymentInstance_PutPost(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView): # restricted
    queryset = Payment.objects.all()
    serializer_class = Pay_ReferencePostPutModelSerializer
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(model_instance, user_info):
        return model_instance.owner.id == user_info.id or user_info.role.role_name == 'admin'

    def delete(self, request,pk, *args, **kargs):
        user_info = get_user_info_from_headers(request)
        payment = Payment.objects.get(id=pk)

        if self.is_owner_or_admin(payment, user_info):
            return self.destroy(request, *args, **kargs)
        else:
            return Response("You cannot delete this item", status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, *args, **kwargs):
        user_info =  user_info = get_user_info_from_headers(request)
        payment = Payment.objects.get(id=pk)

        if self.is_owner_or_admin(payment, user_info):
            return self.update(request, *args, **kwargs)
        else:
            return Response("You cannot modify this item", status=status.HTTP_400_BAD_REQUEST)

class AppointmentInstance(APIView): # restricted
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None): # needed permission
        serializer = AppointmentPostPutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentInstance_PutPost(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView): # restricted
    queryset = Appointment.objects.all()
    serializer_class = AppointmentPostPutSerializer
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(model_instance, user_info):
        return model_instance.client.id == user_info.id or user_info.role.role_name == 'admin'

    def delete(self, request,pk, *args, **kargs): # needed permission
        user_info = get_user_info_from_headers(request)
        appointment = Appointment.objects.get(id=pk)

        if self.is_owner_or_admin(appointment, user_info):
            return self.destroy(request, *args, **kargs)
        else:
            return Response("You cannot delete this item", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):# needed permission
        user_info = get_user_info_from_headers(request)
        appointment = Appointment.objects.get(id=pk)

        if self.is_owner_or_admin(appointment, user_info):
            return self.update(request, *args, **kargs)
        else:
            return Response("You cannot update this item", status=status.HTTP_400_BAD_REQUEST)
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


