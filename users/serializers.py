from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import user

class userSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = user
        fields = ('__all__')


class userSingUpSerializer(serializers.Serializer):
    email =serializers.EmailField()
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    password = serializers.CharField()
    username = serializers.CharField()

    def create(self, validated_data):

        return user.objects.create_user(**validated_data)         