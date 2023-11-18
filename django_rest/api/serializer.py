from rest_framework import serializers
from .models import CompanyModel

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = CompanyModel
        fields ='__all__'