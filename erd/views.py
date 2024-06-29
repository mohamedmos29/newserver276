from .Serializers import pSerializers,ESerializers,ReminderSerializer,DOSerializers,DSerializers,MSerializers,RegisterSerializers,LoginSerializer
from rest_framework import viewsets
from .models import patient,Escort,Medicine,Diseases,Document,Reminder,Register,Login
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework.response import Response


class getLogin(viewsets.ModelViewSet):
    queryset =  Login.objects.all()
    serializer_class = LoginSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer




class GetRegister(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializers

# class GetLogin(viewsets.ModelViewSet):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializers


    

class GetPatient(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = pSerializers
    # def get_extra_actions(self):
    #     return []

class GetEscort(viewsets.ModelViewSet):
    queryset = Escort.objects.all()
    serializer_class = ESerializers

class GetReminder(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class GetDocument(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DOSerializers

class GetMedicine(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MSerializers

class GetDiseases(viewsets.ModelViewSet):
    queryset =Diseases.objects.all()
    serializer_class = DSerializers





