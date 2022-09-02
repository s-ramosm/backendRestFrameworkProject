from ast import Raise
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.serializers import ValidationError

#Serializer
from .serializers import userSerializer,userSingUpSerializer
#Model
from .models import user
from companies.models import company


class userView(viewsets.ModelViewSet):

    permission_classes=[IsAuthenticated]
    serializer_class =  userSerializer
    queryset = user.objects.all()


class userSingUPview(APIView):

    def post(self,request,*args,**kwargs):
        
        serializer = userSingUpSerializer(data = request.data)

        if request.data.get("is_owner", False):
            if (request.user.is_superuser):
                return  Response("You don't have permission to create owners" ,status=401)
            
        if not request.user.is_superuser:
            try:
                _company = company.objects.get_queryset().filter(owner = request.user.id)
                print (_company)
            except:
                return  Response("You don't have company to register users" ,status=401)


        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("created")