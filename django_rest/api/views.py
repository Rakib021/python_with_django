from django.shortcuts import render
from rest_framework import viewsets
from .models import CompanyModel,EmployeeModel
from .serializer import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class =CompanySerializer
    #custom api
    #companies/{companyId}/employees
    
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company = CompanyModel.objects.get(pk =pk)
            emps = EmployeeModel.objects.filter(company = company)
            emps_serializer = EmployeeSerializer(emps,many = True,context ={'request':request})
        
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exits || Error!!!'
            })


        
        
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
