from rest_framework import serializers
from features.core.models import *


class ActSerializer(serializers.ModelSerializer):
    """
    Serializer for Act
    """
    class Meta:
        model = Act
        fields = '__all__'
