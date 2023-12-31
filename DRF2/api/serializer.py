from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=54)
    name = serializers.CharField(max_length=43)
    
  
    def create(self,validate_data):
        return Student.objects.create(**validate_data)