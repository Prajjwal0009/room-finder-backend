from django.db import models

# Create your models here.

#Create Company Models
class Company(models.Model):
    id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','Non IT'),('Mobile Phones','Mobile Phones')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


class Room(models.Model):
   id=models.AutoField(primary_key=True)
   room_type= models.CharField(max_length=100,choices=(('Flat','Flat'),('1Room','1Room'),('2Room','2Room')))
   description=models.TextField()
   location=models.CharField(max_length=50)
   price= models.IntegerField()
   image=models.ImageField(upload_to ='uploads/', blank=True, default='default_image.jpg')
   added_date=models.DateTimeField(auto_now=True)
   
   
class ContactUS(models.Model):
    id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=50)
    message=models.TextField()
  
