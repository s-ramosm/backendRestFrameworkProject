from rest_framework import viewsets

#Serializer
from .serializers import scheduleSerializer
#Model
from .models import schedule


class scheduleView(viewsets.ModelViewSet):

    serializer_class =  scheduleSerializer
    queryset = schedule.objects.all()