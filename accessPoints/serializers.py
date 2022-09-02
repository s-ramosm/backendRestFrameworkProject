from rest_framework import serializers
from .models import accessPoint
from companies.serializers import companySerializer

class accessPointSerializer (serializers.ModelSerializer):

    class Meta:
        model = accessPoint
        fields = '__all__'