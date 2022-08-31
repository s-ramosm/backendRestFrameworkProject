from rest_framework import viewsets

#Serializer
from .serializers import scheduleSerializer
#Model
from .models import schedule


class scheduleView(viewsets.ModelViewSet):

    serializer_class =  schedule
    queryset = schedule.objects.all()