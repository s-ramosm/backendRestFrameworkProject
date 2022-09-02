from rest_framework import serializers
from .models import company
from users.models import user

class companySerializer (serializers.ModelSerializer):

    class Meta:
        model = company
        fields = '__all__'
