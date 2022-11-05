from rest_framework import serializers
from features.core.models import *


class DepositFinanceSerializer(serializers.ModelSerializer):
    """
    Serializer for DepositFinance
    """
    class Meta:
        model = DepositFinance
        fields = '__all__'
