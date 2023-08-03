from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   #return HttpResponse("Hello world")
    return render(request,'pages/index.html')

def about(request):
   x = 10
   y = 30
   food = ['tea','coffee', 'idli']
   students = {"Tom" : 80,"Jerry" : 77,"casper" : 40}
   context = {
    'a' : x,
    'b' : y,
    'food' : food,
    'students' : students,
   }
   return render(request,'pages/about.html',context)
def contactus(request):   
   return render(request,'pages/contactus.html')