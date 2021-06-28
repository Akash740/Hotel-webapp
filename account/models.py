from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class contact_us(models.Model):
    username=models.CharField(max_length=100)
    email= models.EmailField()
    question= models.CharField(max_length=1000)


class roomtype(models.Model):
    
    name=models.CharField(max_length=100)
    decs=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images',default="")

class book_room(models.Model):

    username= models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_people=models.IntegerField()
    no_of_room=models.IntegerField()
    check_in_day=models.DateField()
    check_out_day=models.DateField()
    booking_date=models.DateField(default=timezone.now)
