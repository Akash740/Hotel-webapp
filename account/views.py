from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from account.models import book_room
import time
from account.models import book_room
def reg(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']

        if(password==password and len(password)>5):
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password)
                user.save()
                print("thanks for reg")
        else:
            messages.info(request,"enter the right password")       
    return render(request,'reg.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password2=request.POST['password']
        user=auth.authenticate(username=username,password=password2)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'enter correct username or password')
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def book(request):
    if  request.user.is_authenticated:
        if  request.method=="POST" :
            people=request.POST['people']
            rooms=request.POST['rooms']
            intime=request.POST['inday']
            outtime=request.POST['outday']
            df=User.objects.get(username=request.user.username)
            booking= book_room(username=df,no_of_people=people,no_of_room=rooms,check_in_day=intime,check_out_day=outtime)
            booking.save()
            messages.info(request,'your room has been booked')
            time.sleep(5)
            return redirect('myhotel')
        
           
    else:
        messages.info(request,'for book room you need to login first')
        return redirect('login')
    return render(request,'book_room.html')
 
def booking_details(request):
    book_rooms=book_room.objects.all()
    data_dirct={'booked_room':book_rooms}
    return render(request,'booking_details.html',context=data_dirct)