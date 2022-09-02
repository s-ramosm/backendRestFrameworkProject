from matplotlib.style import use
from rest_framework import serializers
from .models import schedule

from accessPoints.serializers import accessPointSerializer
from users.serializers import userSerializer

class scheduleSerializer (serializers.ModelSerializer):

    access_point = accessPointSerializer(many=True)
    user = userSerializer()

    class Meta:
        model = schedule
        fields = '__all__'