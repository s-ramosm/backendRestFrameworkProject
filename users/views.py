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


from src.mail import send_email


class userView(viewsets.ModelViewSet):

    permission_classes=[IsAuthenticated]
    serializer_class =  userSerializer
    queryset = user.objects.all()

    def create(self, request, *args, **kwargs):

        if request.data.get("is_owner", False):
            if (request.user.is_superuser):
                return  Response("You don't have permission to create owners" ,status=401)
            
        if not request.user.is_superuser:
                _companies = company.objects.get_queryset().filter(owner = request.user.id)
                if len(_companies)==0: return  Response("You don't have company to register users" ,status=401)
        
        if not request.data.get("is_owner", False) and not request.data.get("is_superuser", False):
            
            content = """
                Una cuenta de ususario ha sido creada con nombre {}

                Porfavor ingrese a esta en el sigiente link {}

                su clave es {}
            """.format(request.data.get("username"), "localhost:8000/api-token-auth/", request.data.get("password") )
            
            #send_email(request.data.get("email"), content=content, subject="Dont reply, User registration")

        return super().create(request, *args, **kwargs)


class userSingUPview(APIView):

    def post(self,request,*args,**kwargs):
        
        serializer = userSingUpSerializer(data = request.data)

        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.save())

