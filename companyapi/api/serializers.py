from rest_framework import serializers
from .models import Company,Room,ContactUS



class CompanySerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = '__all__'

class RoomSerializers(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Room
        fields="__all__"


class ContactUSSerializers(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=ContactUS
        fields="__all__"