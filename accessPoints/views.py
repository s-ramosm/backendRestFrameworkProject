from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

#Serializer
from .serializers import accessPointSerializer
#Model
from .models import accessPoint

from rest_framework.permissions import * 

from schedule.models import schedule

import datetime

class accessPointView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]

    serializer_class =  accessPointSerializer
    queryset = accessPoint.objects.all()


    @action(detail=True, methods=['get'])
    def check(self, request, pk=None):

        date = datetime.datetime.now()
        accessPoint = self.get_object()
        user = request.user


        _schedules = schedule.objects.get_queryset().filter(user_id = user.id, access_point = accessPoint.id) \
            .filter(end_time__gte =date.time(), start_time__lte = date.time())
        
        if len(_schedules)==0:
            return Response(False)

        return Response(True)

