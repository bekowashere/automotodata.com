# Generated by Django 4.2.4 on 2023-08-11 20:00

import auto.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Brand Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('image', models.ImageField(upload_to=auto.models.upload_brand_image, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('source_image_path', models.CharField(blank=True, max_length=64, null=True, verbose_name='Source Image Path')),
                ('source_image_url', models.URLField(blank=True, null=True, verbose_name='Source Image URL')),
                ('source_detail_url', models.URLField(blank=True, null=True, verbose_name='Source Detail URL')),
            ],
            options={
                'verbose_name': 'Auto Brand',
                'verbose_name_plural': 'Auto Brands',
            },
        ),
        migrations.CreateModel(
            name='BodyStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Body Style')),
                ('note', models.CharField(blank=True, help_text='(spider/spyder, cabrio/cabriolet, drop/open/soft top)', max_length=255, null=True, verbose_name='Extra Note')),
            ],
            options={
                'verbose_name': 'Body Style',
                'verbose_name_plural': 'Body Styles',
            },
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Fuel Type')),
            ],
            options={
                'verbose_name': 'Fuel Type',
                'verbose_name_plural': 'Fuel Types',
            },
        ),
        migrations.CreateModel(
            name='AutoSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Series Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('image', models.ImageField(upload_to=auto.models.upload_series_image, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('is_discontinued', models.BooleanField(default=False, verbose_name='Discontinued Series')),
                ('source_generation_count', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Source Generation Count')),
                ('source_image_path', models.CharField(blank=True, max_length=64, null=True, verbose_name='Source Image Path')),
                ('source_image_url', models.URLField(blank=True, null=True, verbose_name='Source Image URL')),
                ('source_detail_url', models.URLField(blank=True, null=True, verbose_name='Source Detail URL')),
                ('body_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto.bodystyle', verbose_name='Body Style')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_series', to='auto.autobrand', verbose_name='Brand')),
                ('fuel_type', models.ManyToManyField(blank=True, to='auto.fueltype', verbose_name='Fuel Type')),
            ],
            options={
                'verbose_name': 'Auto Series',
                'verbose_name_plural': 'Auto Series',
            },
        ),
        migrations.CreateModel(
            name='AutoModelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('alt_text', models.CharField(blank=True, max_length=64, null=True, verbose_name='Image Alt Text')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='auto.autobrand', verbose_name='Model')),
            ],
            options={
                'verbose_name': 'Model Image',
                'verbose_name_plural': 'Model Images',
            },
        ),
        migrations.CreateModel(
            name='AutoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Model Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('image', models.ImageField(upload_to=auto.models.upload_model_image, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('source_image_path', models.CharField(blank=True, max_length=64, null=True, verbose_name='Source Image Path')),
                ('source_image_url', models.URLField(blank=True, null=True, verbose_name='Source Image URL')),
                ('source_detail_url', models.URLField(blank=True, null=True, verbose_name='Source Detail URL')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_models', to='auto.autobrand', verbose_name='Brand')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_models', to='auto.autoseries', verbose_name='Series')),
            ],
            options={
                'verbose_name': 'Auto Model',
                'verbose_name_plural': 'Auto Models',
            },
        ),
    ]
