from django.shortcuts import render
from rest_framework import viewsets
from .models import CompanyModel
from .serializer import CompanySerializer

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class =CompanySerializer
    
