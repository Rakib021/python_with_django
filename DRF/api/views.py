from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# Create your views here.



def student_detail(request,pk):
    stu = Student.objects.get(id=pk)

    serializer = StudentSerializer(stu)

    # jsonData= JSONRenderer().render(serializer.data)

    # return HttpResponse(jsonData,content_type="application/json")
    return JsonResponse(serializer.data)


def student_info(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many =True)
    jsonData= JSONRenderer().render(serializer.data)
    return HttpResponse(jsonData,content_type="application/json")
    