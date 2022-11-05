from rest_framework import serializers
from features.core.models import *


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User
    """
    class Meta:
        model = User
        fields = '__all__'
