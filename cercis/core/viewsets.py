from django.db.models import Q
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .filters import KennelFilter, PersonFilter, PoodleFilter
from .models import Image, Kennel, Person, Poodle
from .pagination import LargeResultsSetPagination, StandardResultsSetPagination, OptionsResultsSetPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    ImageSerializer,
    KennelSerializer,
    PersonSerializer,
    PoodleFilterSerializer,
    PoodleSerializer,
)


class PoodleFilterViewSet(ModelViewSet):
    lookup_field = "slug"
    serializer_class = PoodleFilterSerializer
    filterset_class = PoodleFilter
    queryset = Poodle.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = OptionsResultsSetPagination

    def get_queryset(self):
        qs = self.queryset.select_related(
            "color", "origin_country",
            "sire", "dam",
            ).prefetch_related(
            "color", "origin_country",
            "sire", "dam",
            )
        if not self.request.user.is_staff:
            qs = qs.filter(is_viewable=True)
        return qs


class PoodleViewSet(ModelViewSet):
    lookup_field = "slug"
    serializer_class = PoodleSerializer
    queryset = Poodle.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        qs = self.queryset.select_related(
            "color", "origin_country",
            "sire", "dam",
        ).prefetch_related(
            "color", "origin_country",
            "sire", "dam",
        )
        if not self.request.user.is_staff:
            qs = qs.filter(is_viewable=True)
        return qs


class ImageViewSet(ModelViewSet):
    lookup_field = "slug"
    serializer_class = ImageSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Image.objects.all()

    def get_queryset(self):
        poodle = self.request.query_params.get('poodle', None)

        if not self.request.user.is_staff:
            self.queryset = self.queryset.filter(is_viewable=True)

        if poodle is not None:
            self.queryset = self.queryset.filter(poodle__slug=poodle)
        return self.queryset


class PersonViewSet(ModelViewSet):
    lookup_field = "slug"
    serializer_class = PersonSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Person.objects.all()
    filterset_class = PersonFilter
    pagination_class = OptionsResultsSetPagination

    def get_queryset(self):
        qs = self.queryset
        if not self.request.user.is_staff:
            qs = qs.filter(is_viewable=True)
        return qs


class KennelViewSet(ModelViewSet):
    lookup_field = "slug"
    serializer_class = KennelSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Kennel.objects.all()
    filterset_class = KennelFilter

    def get_queryset(self):
        qs = self.queryset
        if not self.request.user.is_staff:
            qs = qs.filter(is_viewable=True)
        return qs
