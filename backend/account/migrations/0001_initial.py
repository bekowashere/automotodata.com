# Generated by Django 4.2.4 on 2023-08-11 20:00

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=128, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Username')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, help_text='Required. 50 characters or fewer. Example: john.doe@gmail.com', max_length=254, unique=True, verbose_name='Email Address')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff User')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_client', models.BooleanField(default=False, verbose_name='Client')),
                ('is_business', models.BooleanField(default=False, verbose_name='Business')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('first_name', models.CharField(blank=True, max_length=64, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=64, verbose_name='Last Name')),
                ('phone_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
