from django.urls import path
from auto.api.views import (
    AutoBrandListAPIView,
    AutoBrandDetailAPIView
)

app_name = 'auto'

urlpatterns = [
    path('', AutoBrandListAPIView.as_view(), name='brand_list'),
    path('<str:slug>', AutoBrandDetailAPIView.as_view(), name='brand_detail'),
]