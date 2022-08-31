from django.shortcuts import render
from rest_framework import viewsets

#Serializer
from .serializers import userSerializer
#Model
from .models import user


class userView(viewsets.ModelViewSet):

    serializer_class =  userSerializer
    queryset = user.objects.all()