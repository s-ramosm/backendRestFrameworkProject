from rest_framework import viewsets

#Serializer
from .serializers import companySerializer
#Model
from .models import company


class companyView(viewsets.ModelViewSet):

    serializer_class =  companySerializer
    queryset = company.objects.all()