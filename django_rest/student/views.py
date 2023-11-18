from django.shortcuts import render
from rest_framework import viewsets
from .models import StudentModel
from .serializer import StudentSerializer

# Create your views here.

class Studentviewset(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer