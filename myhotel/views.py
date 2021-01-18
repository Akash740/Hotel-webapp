from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render 
from account.models import hotel
def myhotel(request):
    hotels = hotel.objects.all()
    return render(request,'index.html',{'hotel':hotels})

def booking (request):
    return render(request,'booking.html')
