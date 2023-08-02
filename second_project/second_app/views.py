from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courses(request):
    return HttpResponse("this is courses page")
def feedback(request):
    return HttpResponse("this is feedback page")
