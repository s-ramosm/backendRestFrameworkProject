from rest_framework import serializers
from .models import accessPoint

class accessPointSerializer (serializers.ModelSerializer):

    class Meta:
        model = accessPoint
        fields = '__all__'