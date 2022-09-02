from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

#Serializer
from .serializers import accessPointSerializer
#Model
from .models import accessPoint

from rest_framework.permissions import * 


class accessPointView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]

    serializer_class =  accessPointSerializer
    queryset = accessPoint.objects.all()


    @action(detail=True, methods=['post'])
    def access(self, request, pk=None):
        accessPoint = self.get_object()
        print(accessPoint)

        return Response("Probando accion")