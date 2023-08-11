from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from auto.models import (
    AutoBrand,
    AutoSeries,
    AutoModel,
    AutoModelImage,
    BodyStyle,
    FuelType
)

@admin.register(AutoBrand)
class AutoBrandAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Information'), {'fields': ('name', 'slug', 'image')}),
        (_('Description'), {'fields': ('description',)}),
        (_('Sources'), {'fields': ('source_image_path', 'source_image_url', 'source_detail_url')})
    )
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name',)

@admin.register(AutoSeries)
class AutoSeriesAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Relationship'), {'fields': ('brand',)}),
        (_('Information'), {'fields': ('name', 'slug', 'image', 'is_discontinued')}),
        (_('Specifications'), {'fields': ('body_style', 'fuel_type')}),
        (_('Sources'), {'fields': ('source_generation_count', 'source_image_path', 'source_image_url', 'source_detail_url')})
    )
    list_display = ('name', 'slug', 'brand')
    search_fields = ('name', 'slug', 'brand__name')
    ordering = ('name',)

@admin.register(AutoModel)
class AutoModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Relationship'), {'fields': ('brand', 'series')}),
        (_('Information'), {'fields': ('name', 'slug', 'image')}),
        (_('Description'), {'fields': ('description',)}),
        (_('Sources'), {'fields': ('source_image_path', 'source_image_url', 'source_detail_url')})
    )
    list_display = ('name', 'slug', 'brand', 'series')
    search_fields = ('name', 'slug', 'brand__name', 'series__name')
    ordering = ('name',)

@admin.register(AutoModelImage)
class AutoModelImageAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Relationship'), {'fields': ('model',)}),
        (_('Information'), {'fields': ('image_url', 'alt_text')}),
    )
    list_display = ('model', 'image_url')
    search_fields = ('model__name', 'image_url', 'alt_text')