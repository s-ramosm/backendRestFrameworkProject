from rest_framework import serializers
from .models import country

class countrySerializer (serializers.ModelSerializer):
    
    

    class Meta:
        model = country
        fields = '__all__'