from rest_framework import serializers
from features.core.models import *


class AffiliateSerializer(serializers.ModelSerializer):
    """
    Serializer for Affiliate
    """
    class Meta:
        model = Affiliate
        fields = '__all__'
