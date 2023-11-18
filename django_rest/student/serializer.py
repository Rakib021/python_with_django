from rest_framework import serializers
from .models import StudentModel


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    student_id = serializers.ReadOnlyField()
    class Meta:
        model =StudentModel
        fields = '__all__'