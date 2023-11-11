from django.shortcuts import render
from .serializers import BookModelSerializer, ArticleModelSerializer, AppointmentTypeModelSerializer, RoleModelSerializer, Pay_MethodModelSerializer, User_infoModelSerializer, Social_mediaModelSerializer, Phone_numberModelSerializer, TagModelSerializer, WriterModelSerializer, SlotModelSerializer, PaymentModelSerializer,Phone_numberModelPostPutSerializer,Social_mediaModelPostPutSerializer, SlotModelPostPutSerializer, AppointmentPostPutSerializer, Pay_ReferencePostPutModelSerializer,AppointmentModelSerializer,SlotCreatorSerializer
from rest_framework import viewsets, status, generics, mixins
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Book, Article, Appointment_type, Role, Pay_method, User_Info, Social_media, Phone_number, Tag, Slot, Writer, Payment, Appointment
from .utils import filter_results_depending_on_role, get_user_id_from_token, get_token_from_headers, get_user_info_from_user_id,get_user_info_from_headers, num_of_days, dates_array
from datetime import time, timedelta, datetime

# Public views
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

class BookInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

class ArticleInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
   
    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

class AppointmentTypeList(generics.ListAPIView):
    queryset = Appointment_type.objects.all()
    serializer_class = AppointmentTypeModelSerializer

class AppointmentTypeInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Appointment_type.objects.all()
    serializer_class = AppointmentTypeModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)

class Pay_methodList(generics.ListAPIView):    
    queryset = Pay_method.objects.all()
    serializer_class = Pay_MethodModelSerializer

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer

class WriterList(generics.ListAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterModelSerializer

class WriterInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Writer.objects.all()
    serializer_class = WriterModelSerializer

    def get(self, request,*args, **kwargs):
        return self.retrieve(self, request,*args, **kwargs)
    

# restricted views: Is needed log in and to have certain role
class RoleList(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleModelSerializer
    permission_classes = [IsAuthenticated]

    
class User_InfoList(generics.ListAPIView):
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


class User_InfoInstance(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = User_Info.objects.all()
    serializer_class = User_infoModelSerializer
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(self, model_instance, user_info):
        return model_instance.id == user_info.id or user_info.role.role_name == 'admin'

    def get(self, request, pk, *args, **kwargs):
        user_info = get_user_info_from_headers(request.headers)
        model_instance = User_Info.objects.get(id=pk)

        if self.is_owner_or_admin(model_instance, user_info):
            return self.destroy(request, *args, **kargs)
        else:
            return Response("You cannot read this item", status=status.HTTP_400_BAD_REQUEST)
        return self.retrieve(self, request,*args, **kwargs)
    
class Social_mediaList(generics.ListAPIView):
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

class Phone_numberList(generics.ListAPIView):
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


class Phone_numberInstance(APIView): 
    permission_classes = [IsAuthenticated]
    
    def is_owner_or_admin(self, instance_owner, user_info):
        return instance_owner == str(user_info.id) or user_info.role.role_name == 'admin'

    def post(self, request, format=None):
        intance_owner = request.data['owner']
        user_info = get_user_info_from_headers(request.headers)
        result = self.is_owner_or_admin(intance_owner, user_info)
        serializer = Phone_numberModelPostPutSerializer(data = request.data)
        if serializer.is_valid() and self.is_owner_or_admin(intance_owner, user_info):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else: 
            if serializer.errors:
                   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response("You don't have permission to create this item", status=status.HTTP_400_BAD_REQUEST)


class Phone_numberInstanceDeletePut(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView): # restricted
    queryset = Phone_number.objects.all()
    serializer_class = Phone_numberModelPostPutSerializer
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(self, model_instance, user_info):
        return model_instance.owner.id == user_info.id or user_info.role.role_name == 'admin'

    def delete(self, request,pk, *args, **kwargs):
        user_info = get_user_info_from_headers(request.headers)
        phone_number = Phone_number.objects.get(id=pk)

        if self.is_owner_or_admin(phone_number, user_info):
            return self.destroy(request, *args, **kwargs)
        else:
            return Response("You cannot delete this item", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk, *args, **kwargs):
        user_info = get_user_info_from_headers(request.headers)
        phone_number = Phone_number.objects.get(id=pk)

        if self.is_owner_or_admin(phone_number, user_info):
            return self.update(request, *args, **kwargs)
        else:
            return Response("You cannot update this item", status=status.HTTP_400_BAD_REQUEST)

class Social_mediaInstance(APIView):
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(self, instance_owner, user_info):
        return instance_owner == str(user_info.id) or user_info.role.role_name == 'admin'

    def post(self, request, format=None):
        intance_owner = request.data['owner']
        user_info = get_user_info_from_headers(request.headers)
        result = self.is_owner_or_admin(intance_owner, user_info)
        serializer = Social_mediaModelPostPutSerializer(data = request.data)
        if serializer.is_valid() and self.is_owner_or_admin(intance_owner, user_info):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:    
            if serializer.errors:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response("You don't have permission to create this item", status=status.HTTP_400_BAD_REQUEST)

class Social_mediaInstanceDeletePut(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Social_media.objects.all()
    serializer_class = Social_mediaModelPostPutSerializer
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(self, model_instance, user_info):
        return model_instance.owner.id == user_info.id or user_info.role.role_name == 'admin'

    def delete(self, request,pk, *args, **kwargs):
        user_info = get_user_info_from_headers(request.headers)
        social_media_instance = Social_media.objects.get(id=pk)

        if self.is_owner_or_admin(social_media_instance, user_info):
            return self.destroy(request, *args, **kwargs)
        else:
            return Response("You cannot delete this item", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk, *args, **kwargs):
        user_info = get_user_info_from_headers(request.headers)
        social_media_instance = Social_media.objects.get(id=pk)

        if self.is_owner_or_admin(social_media_instance, user_info):
            return self.update(request, *args, **kwargs)
        else:
            return Response("You cannot update this item", status=status.HTTP_400_BAD_REQUEST)
class SlotInstance(APIView):#restricted
    permission_classes = [IsAuthenticated]

    def not_client(self,user_info):
        return user_info.role.role_name != 'client'

    def is_owner_or_admin(self, instance_owner, user_info):
        return instance_owner == str(user_info.id) or user_info.role.role_name == 'admin' 

    def post(self, request, format=None): # needed permission
        user_info = get_user_info_from_headers(request.headers)

        if self.not_client(user_info=user_info):
            serializer = SlotModelPostPutSerializer(data = request.data)
            intance_owner = request.data['owner']
            if serializer.is_valid() and self.is_owner_or_admin(intance_owner, user_info):
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                if serializer.errors:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response("You cannot create this item", status=status.HTTP_400_BAD_REQUEST)
        return Response("You cannot create this item", status=status.HTTP_400_BAD_REQUEST)

class SlotInstance_PutPost(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):# restricted
    queryset = Slot.objects.all()
    serializer_class = SlotModelPostPutSerializer
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(self, model_instance, user_info):
        return model_instance.owner.id == user_info.id or user_info.role.role_name == 'admin'

    def delete(self, request,pk, *args, **kwargs): 
        user_info = get_user_info_from_headers(request.headers)
        slot = Slot.objects.get(id=pk)

        if self.is_owner_or_admin(slot, user_info):
            return self.destroy(request, *args, **kwargs)
        else:
            return Response("You cannot delete this item", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        user_info = get_user_info_from_headers(request.headers)
        slot = Slot.objects.get(id=pk)

        if self.is_owner_or_admin(slot, user_info):
            return self.update(request, *args, **kwargs)
        else:
            return Response("You cannot update this item", status=status.HTTP_400_BAD_REQUEST)

class SlotList(generics.ListAPIView):
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


class PaymentList(generics.ListAPIView):
    serializer_class = PaymentModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
       
        def admin_action(user_info):
            return Payment.objects.all()

        def client_action(user_info):
            return Payment.objects.filter(owner=user_info.id)
        
        def psico_action(user_info):
            return Payment.objects.none()

        return filter_results_depending_on_role(self.request.headers, admin_action=admin_action, client_action=client_action, psico_action=psico_action)

class PaymentInstance(APIView): # this should be protected
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentModelSerializer

    def not_psico(self,user_info):
        return user_info.role.role_name != 'psico'
    
    def is_owner_or_admin(self, instance_owner, user_info):
        return instance_owner == str(user_info.id) or user_info.role.role_name == 'admin'
    
    def post(self, request,format=None): # needed permission
        user_info = get_user_info_from_headers(request.headers)
        if self.not_psico(user_info):
            intance_owner = request.data['owner']
            print(request.data)
            serializer = Pay_ReferencePostPutModelSerializer(data = request.data)

            if serializer.is_valid() and self.is_owner_or_admin(intance_owner,user_info):
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                if serializer.errors:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response("You cannot create this item", status=status.HTTP_400_BAD_REQUEST)
        return Response("You cannot create this item", status=status.HTTP_400_BAD_REQUEST)
class PaymentInstance_PutPost(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView): # restricted
    queryset = Payment.objects.all()
    serializer_class = Pay_ReferencePostPutModelSerializer
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(self, model_instance, user_info):
        return model_instance.owner.id == user_info.id or user_info.role.role_name == 'admin'

    def delete(self, request,pk, *args, **kwargs):
        user_info = get_user_info_from_headers(request.headers)
        payment = Payment.objects.get(id=pk)

        if self.is_owner_or_admin(payment, user_info):
            return self.destroy(request, *args, **kwargs)
        else:
            return Response("You cannot delete this item", status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, *args, **kwargs):
        user_info =  user_info = get_user_info_from_headers(request.headers)
        payment = Payment.objects.get(id=pk)

        if self.is_owner_or_admin(payment, user_info):
            return self.update(request, *args, **kwargs)
        else:
            return Response("You cannot modify this item", status=status.HTTP_400_BAD_REQUEST)

class AppointmentInstance(APIView): # restricted
    permission_classes = [IsAuthenticated]

    def not_psico(self,user_info):
        return user_info.role.role_name != 'psico'
    
    def is_owner_or_admin(self, instance_owner, user_info):
        print(instance_owner, user_info.id)
        return instance_owner == str(user_info.id) or user_info.role.role_name == 'admin'
    
    def post(self, request, format=None): # needed permission
        user_info = get_user_info_from_headers(request.headers)

        if self.not_psico(user_info):
            intance_owner = request.data['client']
            serializer = AppointmentPostPutSerializer(data = request.data)
            if serializer.is_valid() and self.is_owner_or_admin(intance_owner,user_info):
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            else:
                if serializer.errors:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response("You cannot create this item", status=status.HTTP_400_BAD_REQUEST)
        return Response("You cannot create this item", status=status.HTTP_400_BAD_REQUEST)

class AppointmentInstance_PutPost(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView): # restricted
    queryset = Appointment.objects.all()
    serializer_class = AppointmentPostPutSerializer
    permission_classes = [IsAuthenticated]

    def is_owner_or_admin(self, model_instance, user_info):
        return model_instance.client.id == user_info.id or user_info.role.role_name == 'admin'

    def delete(self, request,pk, *args, **kwargs):
        user_info = get_user_info_from_headers(request.headers)
        appointment = Appointment.objects.get(id=pk)

        if self.is_owner_or_admin(appointment, user_info):
            return self.destroy(request, *args, **kwargs)
        else:
            return Response("You cannot delete this item", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk, *args, **kwargs):
        user_info = get_user_info_from_headers(request.headers)
        appointment = Appointment.objects.get(id=pk)

        if self.is_owner_or_admin(appointment, user_info):
            return self.update(request, *args, **kwargs)
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


##
# #def create_zoom_meeting(request):
#     # Initialize Zoom API client with your credentials
#     zoom_client = ZoomClient(api_key='YOUR_ZOOM_API_KEY', api_secret='YOUR_ZOOM_API_SECRET')

#     # Create Zoom meeting parameters
#     meeting_params = {
#         "topic": "My Meeting",
#         "type": 2,
#         "start_time": "2023-11-11T10:00:00",
#         "duration": 60,
#         "timezone": "America/New_York",
#         "password": "123456"
#     }

#     # Create the Zoom meeting
#     meeting = zoom_client.meetings.create(**meeting_params)

#     # Generate join URL for the meeting
#     join_url = meeting['join_url']

#     # Send email invitations to participants
#     # Replace 'participants' with a list of email addresses
#     participants = ['participant1@email.com', 'participant2@email.com']
#     for participant in participants:
#         send_zoom_meeting_invitation(participant, join_url)

#     return HttpResponse('Meeting created successfully!')

# ##
class SlotCreator(APIView):
    permission_classes = [IsAuthenticated]
    
    def not_client(self,user_info):
        return user_info.role.role_name != 'client'


    def post(self, request, format=None): # needed permission
        user_info = get_user_info_from_headers(request.headers)
        if self.not_client(user_info):
            serializer = SlotCreatorSerializer(data = request.data)
            if serializer.is_valid():
                # here start the algorithm
                
                num_days = num_of_days(request.data['start_date'], request.data['end_date'])

                dates = dates_array(num_days, request.data['start_date'])

                start_day = request.data['start_day'].split(":")
                end_day =  request.data["end_day"].split(":")

                for date in dates:
                    start_work_date= datetime.combine(date, time(hour=int(start_day[0]), minute=int(start_day[1]))) 
                    end_work_date = datetime.combine(date, time(hour=int(end_day[0]), minute=int(end_day[1])))

                    current_time =  start_work_date
                    while current_time < end_work_date:
                        slot_duration = timedelta(minutes=int(request.data['slot_duration']))
                        current_time = current_time + slot_duration
                        print(current_time, "current time")


                # current_date = request.data["start_date"]
                # end_day =  request.data["end_day"].split(":")
                # initial_time = request.data['start_day'].split(":")

                # for i in range(num_days):

                #     current_time = datetime.combine(datetime.now(), time(hour=int(initial_time[0]), minute=int(initial_time[1]))) 
                #     current_end_date = datetime.combine(datetime.now(), time(hour=int(end_day[0]), minute=int(end_day[1]))) 
                #     slot_duration = timedelta(minutes=int(request.data['slot_duration']))
                #     result = current_time + slot_duration
                #     print(current_time, current_end_date)
                #     if result < current_end_date:
                #         print("is less")

                    
                #     # if current time plus slot time is less than end day
                #     # create an slot 
                #     # plus slot time to current time
                #     number_of_hours = 3

                return Response("Fucking error", status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
