from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render 
from account.models import contact_us,roomtype
def myhotel(request):
    room=roomtype.objects.all()
    data_dirct={'rooms':room}
    return render(request,'index.html',context=data_dirct)


def contact(request):
    if request.method=='POST':
        username=request.POST['enter_name']
        email=request.POST['email']
        question= request.POST['question']
        ins= contact_us(username=username,email=email,question=question)
        ins.save()  
    return render(request,'contact.html')

def room_view(request,id):
    room=roomtype.objects.filter(id=id)
    data_dirct={'rooms':room[0]}

    return render(request,'room_view.html',context=data_dirct)