from django.shortcuts import render
from django.http import HttpResponse
from ArtBase.models import *

def home(request):
    obj=paintings.objects.all()
    data={
        "obj":obj 
    }
    return render(request,'index.html',data)

def contactus(request):
    if request.method=='POST':
        name=request.POST.get('nam')
        num=request.POST.get('num')
        msg=request.POST.get('msg')
        con=contact(name=name,num=num,msg=msg)
        con.save()
    return render(request,'contact.html')

def booksketch(request):
    if request.method=='POST':
        name=request.POST.get('nam')
        num=request.POST.get('num')
        img=request.POST.get('img')
        qu=book(name=name,num=num,img=img)
        qu.save()
    return render(request,'bookSketch.html')


def fee(request):
    if request.method=='POST':
        name=request.POST.get('name')
        msg=request.POST.get('feed')
        qu=feedback(name=name,msg=msg)
        qu.save()
    return render(request,'feed.html')






