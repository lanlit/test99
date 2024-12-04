from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy

# Create your views here.
# def A(request):
#     courses = course.objects.all()
#     return render(request,"list.html",{"A":courses})
 
def c(request):
    name = request.GET.get("name","")
    C = course.objects.filter(name=name)
    return render(request,"C.html", {"C":C})

 
    





