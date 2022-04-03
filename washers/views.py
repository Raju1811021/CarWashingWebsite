from django import forms
from django.shortcuts import render
from washers import forms,models
from django.http import HttpResponse
from django.contrib import messages
def check(request):
    return render(request,'washer/home.html')
def findprice(request):
    suggest=models.carprice.objects.all()
    data={'suggest':suggest}
    return render(request,'washer/findprice.html',data)
def getprice(request):
    data=request.GET['carname']
    price1=models.carprice.objects.filter(carname=data)
    for p in price1:
        price=p.price
    else:
        price=500
    suggest=models.carprice.objects.all()
    return render(request,'washer/findprice.html',{'price':price,'suggest':suggest})
def take_service(request):
    book_form=forms.registratio_form()
    return render(request,'washer/wash_registration.html',{'booking_form':book_form})
def SaveBookingData(request):
    if request.method=='POST':
        formdata=forms.registratio_form(request.POST)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,'Registration Successful,We will contact you soon within 48 hours , thanks for registration.')
            return render(request,'washer/wash_registration.html',{'booking_form':formdata})
        else:
            return render(request,'washer/wash_registration.html',{'booking_form':formdata})
    else:
        return render(request,'washer/home.html')  
def payment(request):
    return render(request,'washer/payment.html')