from rest_framework import viewsets

#Serializer
from .serializers import countrySerializer
#Model
from .models import country


class countryView(viewsets.ModelViewSet):

    serializer_class =  countrySerializer
    queryset = country.objects.all()