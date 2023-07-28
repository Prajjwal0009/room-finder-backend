from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Room,ContactUS
from api.serializers import CompanySerializer,RoomSerializers,ContactUSSerializers

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer


class RoomViewSet(viewsets.ModelViewSet):
 queryset=Room.objects.all()
 serializer_class=RoomSerializers   


class ContactUSViewSet(viewsets.ModelViewSet):
 queryset=ContactUS.objects.all()
 serializer_class=ContactUSSerializers       