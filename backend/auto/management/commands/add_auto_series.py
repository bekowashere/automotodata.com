from django.core.management import BaseCommand, CommandError
from auto.models import AutoBrand, AutoSeries, BodyStyle, FuelType
import json

class Command(BaseCommand):
    """
    AutoBrand:
        brand
        name
        slug
        image
        body_style
        fuel_type
        is_discontinued
        source_generation_count
        source_image_path
        source_image_url
        source_detail_url
    JSON:
        brand_name
        brand_detail_url
        brand_slug
        series_name
        series_slug
        series_image_path
        series_image_url
        series_bodyStyle
        series_fuelType
        series_isDiscontinued
        series_generation_count
        series_detail_url
    """

    def handle(self, *args, **options):
        file_path = '_data/auto/all_series.json'

        with open(file_path, 'r', encoding="UTF-8") as f:
            data = json.load(f)

        for obj in data:
            if obj['series_bodyStyle'] is not None:
                try:
                    b_style = BodyStyle.objects.get(name=obj['series_bodyStyle'])
                except BodyStyle.DoesNotExist:
                    b_style = BodyStyle(name=obj['series_bodyStyle'])
                    b_style.save()

            try:
                new_object = AutoSeries(
                    brand=AutoBrand.objects.get(slug=obj['brand_slug']),
                    name=obj['series_name'],
                    slug=obj['series_slug'],
                    image=f"auto/{obj['brand_name']}/{obj['series_name']}/{obj['series_image_path']}",
                    body_style = b_style,
                    is_discontinued = obj['series_isDiscontinued'],
                    source_generation_count = obj['series_generation_count'],
                    source_image_path = obj['series_image_path'],
                    source_image_url = obj['series_image_url'],
                    source_detail_url = obj['series_detail_url']
                )
                new_object.save()

                if len(obj['series_fuelType']) > 0:
                    for fuel in obj['series_fuelType']:
                        try:
                            fueltype = FuelType.objects.get(name=fuel)
                        except FuelType.DoesNotExist:
                            fueltype = FuelType(name=fuel)
                            fueltype.save()
                        new_object.fuel_type.add(fueltype)
                
                new_object.save()

                self.stdout.write(self.style.SUCCESS(f'{new_object.name} create successfully'))
            except Exception as e:
                raise CommandError(f'{e}')
