from django.db.models import CharField
from django_filters import CharFilter, FilterSet

from .forms import ColorFilterForm, CountryFilterForm
from .models import Color, Country


class ColorFilter(FilterSet):

    class Meta:
        model = Color
        form = ColorFilterForm
        fields = [
            'text',
        ]
        filter_overrides = {
            CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }


class CountryFilter(FilterSet):

    class Meta:
        model = Country
        form = CountryFilterForm
        fields = [
            'text',
            'code',
        ]
        filter_overrides = {
            CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }
