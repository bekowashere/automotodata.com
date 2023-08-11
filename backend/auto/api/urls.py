from django.urls import path
from auto.api.views import (
    AutoBrandListAPIView
)

app_name = 'auto'

urlpatterns = [
    path('', AutoBrandListAPIView.as_view(), name='brand_list'),
]