from rest_framework import serializers
from features.core.models import *

class UnionSectionSerializer(serializers.ModelSerializer):
    """
    Serializer for UnionSection
    """

    class Meta:
        model = UnionSection
        fields = '__all__'
        depth = 1
