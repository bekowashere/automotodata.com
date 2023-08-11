from rest_framework import serializers
from auto.models import (
    AutoBrand,
    AutoSeries,
    AutoModel,
    AutoModelImage
)

class AutoBrandListSerializer(serializers.ModelSerializer):
    series_total_count = serializers.SerializerMethodField()
    series_continued_count = serializers.SerializerMethodField()
    series_discontinued_count = serializers.SerializerMethodField()
    # brand_url = serializers.HyperlinkedIdentityField(
    #     view_name='auto:brand_detail',
    #     lookup_field='brand_slug'
    # )

    def get_series_total_count(self, obj):
        return obj.get_total_series_count
    
    def get_series_continued_count(self, obj):
        return obj.get_continued_series_count
    
    def get_series_discontinued_count(self, obj):
        return obj.get_discontinued_series_count
    
    class Meta:
        model = AutoBrand
        fields = (
            'id',
            'name',
            'slug',
            'image',
            'source_image_path',
            'source_image_url',
            'source_detail_url',
            'series_total_count',
            'series_continued_count',
            'series_discontinued_count'
        )