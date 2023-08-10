from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

# class BodyStyle
# class FuelType
# class Infotainment

# class DriveType
# class GearBox

def upload_brand_image(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    return f"brands/{instance.name}/logo.{extension}"

class AutoBrand(models.Model):
    name = models.CharField(_('Brand Name'), max_length=64)
    slug = models.SlugField(_('Slug'), unique=True)
    image = models.ImageField(
        upload_to=upload_brand_image,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    description = models.TextField(_('Description'), null=True, blank=True)

    # Source
    source_image_path = models.CharField(_('Source Image Path'), null=True, blank=True)
    source_image_url = models.URLField(_('Source Image URL') ,null=True, blank=True)
    source_detail_url = models.URLField(_('Source Detail URL') ,null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('Auto Brand')
        verbose_name_plural = _('Auto Brands')

def upload_series_image(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    return f"brands/{instance.brand.name}/{instance.name}/{instance.name}.{extension}"

class AutoSeries(models.Model):
    # EXTEND FK
    brand = models.ForeignKey(
        AutoBrand,
        on_delete=models.CASCADE,
        verbose_name=_('Brand'),
        related_name='brand_series'
    )

    # Main
    name = models.CharField(_('Series Name'), max_length=64)
    slug = models.SlugField(_('Slug'))
    image = models.ImageField(
        upload_to=upload_series_image,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )

    # FK BodyStyle
    # M2M FuelType

    is_discontinued = models.BooleanField(_('Discontinued Series'), default=False)

    # Source
    source_generation_count = models.PositiveSmallIntegerField(
        _('Source Generation Count'),
        null=True,
        blank=True
    )
    source_image_path = models.CharField(_('Source Image Path'), null=True, blank=True)
    source_image_url = models.URLField(_('Source Image URL') ,null=True, blank=True)
    source_detail_url = models.URLField(_('Source Detail URL') ,null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('Series')
        verbose_name_plural = _('Series')

def upload_model_image(instance, filename):
    filebase, extension = filename.rsplit('.', 1)
    return f"brands/{instance.brand.name}/{instance.series.name}/{instance.name}/{instance.name}.{extension}"

class AutoModel(models.Model):
    # EXTEND FK
    brand = models.ForeignKey(
        AutoBrand,
        on_delete=models.CASCADE,
        verbose_name=_('Brand'),
        related_name='brand_models'
    )
    series = models.ForeignKey(
        AutoSeries,
        on_delete=models.CASCADE,
        verbose_name=_('Series'),
        related_name='series_models'
    )

    # Main
    name = models.CharField(_('Series Name'), max_length=64)
    slug = models.SlugField(_('Slug'))
    image = models.ImageField(
        upload_to=upload_model_image,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    description = models.TextField(_('Description'), null=True, blank=True)

    # YEARS
    # start_year
    # end_year
    # years M2M -> ModelYear (jsonda strip yapmalı)

    # FK Segment
    # M2M FuelType
    # M2M Infotainment

    # Source
    source_image_path = models.CharField(_('Source Image Path'), max_length=64, null=True, blank=True)
    source_image_url = models.URLField(_('Source Image URL') ,null=True, blank=True)
    source_detail_url = models.URLField(_('Source Detail URL') ,null=True, blank=True)

class AutoModelImage(models.Model):
    model = models.ForeignKey(
        AutoBrand,
        on_delete=models.CASCADE,
        verbose_name=_('Model'),
        related_name='images'
    )

    image_url = models.URLField(_('Image URL'))
    alt_text = models.CharField(_('Image Alt Text'), null=True, blank=True)

    def __str__(self) -> str:
        return self.model.name
    
    class Meta:
        verbose_nmae = _('Model Image')
        verbose_nmae_plural = _('Model Images')