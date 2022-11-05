from rest_framework import serializers
from features.core.models import *


class AgreementSerializer(serializers.ModelSerializer):
    """
    Serializer for Agreement
    """
    class Meta:
        model = Agreement
        fields = '__all__'
