from rest_framework import serializers
from .models import user

class userSerializer (serializers.ModelSerializer):
    
    

    class Meta:
        model = user
        fields = ('email', 'last_name', 'first_name', 'password', "is_staff","username")