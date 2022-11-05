from rest_framework import serializers
from features.core.models import *


class ApproachSerializer(serializers.ModelSerializer):
    """
    Serializer for Approach
    """
    class Meta:
        model = Approach
        fields = '__all__'
