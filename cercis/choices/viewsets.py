from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from .filters import ColorFilter, CountryFilter
from .models import Color, Country
from .pagination import StandardResultsSetPagination, LargeResultsSetPagination
from .serializers import ColorSerializer, CountrySerializer


class ColorViewSet(ModelViewSet):
    lookup_field = "slug"
    serializer_class = ColorSerializer
    queryset = Color.objects.filter(is_active=True)
    pagination_class = StandardResultsSetPagination
    filterset_class = ColorFilter

    def get_queryset(self):
        qs = self.queryset
        if not self.request.user.is_staff:
            qs = qs.filter(is_active=True)
        return qs


class CountryViewSet(ModelViewSet):
    lookup_field = "slug"
    serializer_class = CountrySerializer
    queryset = Country.objects.filter(is_active=True)
    pagination_class = LargeResultsSetPagination
    filterset_class = CountryFilter

    def get_queryset(self):
        qs = self.queryset
        if not self.request.user.is_staff:
            qs = qs.filter(is_active=True)
        return qs
