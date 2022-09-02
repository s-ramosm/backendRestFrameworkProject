from rest_framework import viewsets

#Serializer
from .serializers import stateSerializer
#Model
from .models import state


class stateView(viewsets.ModelViewSet):

    serializer_class =  stateSerializer
    queryset = state.objects.all()


