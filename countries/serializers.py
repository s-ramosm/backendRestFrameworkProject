from rest_framework import serializers
from .models import country
from users.models import user

class countrySerializer (serializers.ModelSerializer):
    
    

    class Meta:
        model = country
        fields = '__all__'
