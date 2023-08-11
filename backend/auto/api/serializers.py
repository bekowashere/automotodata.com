from rest_framework import serializers
from auto.models import (
    AutoBrand,
    AutoSeries,
    AutoModel,
    AutoModelImage
)

class AutoBrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoBrand
        fields = '__all__'