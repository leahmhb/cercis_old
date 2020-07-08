from django.db.models import CharField
from django_filters import CharFilter, FilterSet

from .forms import ColorFilterForm, CountryFilterForm, TitleFilterForm
from .models import Color, Country, Title


class TitleFilter(FilterSet):

    class Meta:
        model = Title
        form = TitleFilterForm
        fields = [
            'abbr',
        ]
        filter_overrides = {
            CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }

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
