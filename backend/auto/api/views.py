"""
/auto : BrandListSerializer
/auto/<brand_slug> : BrandDetailSerializer
/auto/<brand_slug>/<series_slug> : SeriesDetailSerializer
/auto/<brand_slug>/<series_slug>/<model_slug> : ModelDetailSerializer
/cars/<car_slug> : CarDetailSerializer
"""
# Cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

# Rest Framework Helpers
from rest_framework.response import Response
from rest_framework import status

# Rest Framework Views
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

# Permissions
from rest_framework.permissions import IsAuthenticated

from auto.api.serializers import (
    AutoBrandListSerializer,
    AutoBrandDetailSerializer
)

from auto.models import (
    AutoBrand,
    AutoSeries,
    AutoModel,
    AutoModelImage
)

class AutoBrandListAPIView(ListAPIView):
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [SubscriptionDailyRateThrottle]

    queryset = AutoBrand.objects.all()
    serializer_class = AutoBrandListSerializer

class AutoBrandDetailAPIView(RetrieveAPIView):
    queryset = AutoBrand.objects.all()
    serializer_class = AutoBrandDetailSerializer
    lookup_field = 'slug'