from rest_framework import serializers
from .models import schedule

class scheduleSerializer (serializers.ModelSerializer):

    class Meta:
        model = schedule
        fields = '__all__'