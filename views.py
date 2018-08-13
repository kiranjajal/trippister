from django.shortcuts import render,redirect
from .models import overview,itinerary,location,reviews
#from home.data import homeData
import json
# Create your views here.
def index(request):

    if request.method=='GET':
        return render(request,'home/index.html')


def over(request):
    content=overview.objects.all()
  #  for i in content:
   #     d=json.loads(str(i))
    #    print(d['name'])
   # print(content)
    #print(d['content'])
    if request.method=='GET':
        return render(request,'home/index.html',{'content':content})

def itin(request):
    content1=str(itin.objects.all())
    if request.method=='GET':
        return render(request,'home/index.html',{'content':content1})

def loc(request):
    content2=str(loc.objects.all())
    if request.method=='GET':
        return render(request,'home/index.html',{'content':content2})

def rev(request):
    content3=str(rev.objects.all())
    if request.method=='GET':
        return render(request,'home/index.html',{'content':content3})

