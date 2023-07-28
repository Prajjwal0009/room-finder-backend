from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,RoomViewSet,ContactUSViewSet
from rest_framework import routers



router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'room',RoomViewSet)
router.register(r'contact-us',ContactUSViewSet)




urlpatterns = [
path('',include(router.urls))


]