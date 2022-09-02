from rest_framework import serializers
from .models import state

class stateSerializer (serializers.ModelSerializer):

    class Meta:
        model = state
        fields = '__all__'