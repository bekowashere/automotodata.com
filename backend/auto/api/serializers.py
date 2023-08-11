from rest_framework import serializers
from auto.models import (
    AutoBrand,
    AutoSeries,
    AutoModel,
    AutoModelImage,
    BodyStyle,
    FuelType
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

class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = ('id', 'name')

class AutoSeriesListSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    body_style = serializers.SerializerMethodField()
    fuel_type = FuelTypeSerializer(many=True)
    generation_count = serializers.SerializerMethodField()

    def get_brand(self, obj):
        return obj.brand.name

    def get_body_style(self, obj):
        return obj.body_style.name
    
    def get_generation_count(self, obj):
        return obj.get_models_count
    
    class Meta:
        model = AutoSeries
        fields = (
            'id',
            'brand',
            'name',
            'slug',
            'image',
            'body_style',
            'fuel_type',
            'is_discontinued',
            'generation_count',
            'source_generation_count',
            'source_image_path',
            'source_image_url',
            'source_detail_url',
        )

class AutoBrandDetailSerializer(serializers.ModelSerializer):
    series_total_count = serializers.SerializerMethodField()
    series_continued_count = serializers.SerializerMethodField()
    series_discontinued_count = serializers.SerializerMethodField()
    
    in_production = serializers.SerializerMethodField()
    discontinued = serializers.SerializerMethodField()

    def get_series_total_count(self, obj):
        return obj.get_total_series_count
    
    def get_series_continued_count(self, obj):
        return obj.get_continued_series_count
    
    def get_series_discontinued_count(self, obj):
        return obj.get_discontinued_series_count
    
    def get_in_production(self, obj):
        return AutoSeriesListSerializer(obj.get_continued_series, many=True).data
    
    def get_discontinued(self, obj):
        return AutoSeriesListSerializer(obj.get_discontinued_series, many=True).data
    
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
            'series_discontinued_count',
            'in_production',
            'discontinued',
            'description'
        )