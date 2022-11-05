from rest_framework import serializers
from features.core.models import *


class ContributionDepositSerializer(serializers.ModelSerializer):
    """
    Serializer for ContributionDeposit
    """
    class Meta:
        model = ContributionDeposit
        fields = '__all__'
