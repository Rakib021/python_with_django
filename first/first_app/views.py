from django.shortcuts import render

from django.http import HttpResponse

def home (request):
    return HttpResponse ("<h1>hello this is home page</h1>")

def about (request):
    return HttpResponse ("hello this is about page")
