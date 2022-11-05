from rest_framework import serializers
from features.core.models import *


class DonationSerializer(serializers.ModelSerializer):
    """
    Serializer for Donation
    """
    class Meta:
        model = Donation
        fields = '__all__'
