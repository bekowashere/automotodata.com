from django.core.management import BaseCommand, CommandError
from auto.models import AutoBrand
import json

class Command(BaseCommand):
    """
    AutoBrand:
        name
        slug
        image
        description
        source_image_path
        source_image_url
        source_detail_url
    JSON:
        brand_name
        brand_slug
        brand_image_path
        brand_image_url
        brand_detail_url
        brand_description
    """

    def handle(self, *args, **options):
        file_path = '_data/auto/all_brands.json'

        with open(file_path, 'r', encoding="UTF-8") as f:
            data = json.load(f)

        for obj in data:
            try:
                new_object = AutoBrand(
                    name=obj['brand_name'],
                    slug=obj['brand_slug'],
                    image=f"auto/{obj['brand_name']}/{obj['brand_image_path']}",
                    description=obj['brand_description'],
                    source_image_path = obj['brand_image_path'],
                    source_image_url = obj['brand_image_url'],
                    source_detail_url = obj['brand_detail_url']
                )
                new_object.save()

                self.stdout.write(self.style.SUCCESS(f'{new_object.name} create successfully'))
            except Exception as e:
                raise CommandError(f'{e}')
