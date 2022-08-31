from django.shortcuts import render
from rest_framework import viewsets

#Serializer
from .serializers import accessPointSerializer
#Model
from .models import accessPoint


class accessPointView(viewsets.ModelViewSet):

    serializer_class =  accessPointSerializer
    queryset = accessPoint.objects.all()