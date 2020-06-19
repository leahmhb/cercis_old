from django.db.models import CharField, Q
from django_filters import CharFilter, FilterSet

from .forms import KennelFilterForm, PersonFilterForm, PoodleFilterForm
from .models import Kennel, Person, Poodle


def q_owners(request):
    n = request.query_params.get('owners', None)
    if n is not None:
        return Person.objects.filter(full_name__contains=n)
    return Person.objects.none()


def q_breeders(request):
    n = request.query_params.get('breeders', None)
    if n is not None:
        return Person.objects.filter(full_name__contains=n)
    return Person.objects.none()


def q_siblings(request):
    siblingsof = request.query_params.get('siblingsof', None)
    if siblingsof is not None:
        poodle = Poodle.objects.filter(slug=siblingsof).values('sire', 'dam')
        sire = poodle.sire
        print(sire)
        dam = poodle.dam
        print(dam)

        qs = Poodle.objects.exclude(
                slug=siblingsof
        ).filter(
            Q(sire_id=sire) | Q(dam_id=dam)
        )
        return qs
    else:
        return Poodle.objects.none()


def q_sib_type(request):
    siblingsof = request.query_params.get('siblingsof', None)
    if siblingsof is not None:
        poodle = Poodle.objects.filter(slug=siblingsof).values('sire', 'dam')
        sire = poodle.sire.id
        dam = poodle.dam.id
    else:
        return Poodle.objects.none()

    sib_type = request.query_params.get('sib_type', None)
    if sib_type is not None:
        qs = Poodle.objects.exclude(
            slug=siblingsof
        )
        if sib_type == 'full':
            qs = qs.filter(
                Q(sire_id=sire) & Q(dam_id=dam)
            )
        elif sib_type == 'damside':
            qs = qs.filter(
                ~ Q(sire_id=sire) & Q(dam_id=dam)
            )
        elif sib_type == 'sireside':
            qs = qs.filter(
                Q(sire_id=sire) & ~Q(dam_id=dam)
            )
        return qs
    else:
        return Poodle.objects.none()


class PoodleFilter(FilterSet):
    owners = CharFilter(field_name='owners__full_name', lookup_expr='icontains')
    breeders = CharFilter(field_name="breeders__full_name", lookup_expr='icontains')
    origin_country = CharFilter(field_name='origin_country__text', lookup_expr='icontains')

    class Meta:
        model = Poodle
        form = PoodleFilterForm
        fields = [
                    'name_registered',
                    'name_call',
                    'variety',
                    'color',
                    'akc',
                    'ukc',
                    'addtl',
                    'owners',
                    'breeders',
                    'origin_country',
                    'created_by'
                 ]
        filter_overrides = {
            CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }


class PersonFilter(FilterSet):

    class Meta:
        model = Person
        form = PersonFilterForm
        fields = [
            'full_name',
        ]
        filter_overrides = {
            CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }


class KennelFilter(FilterSet):

    class Meta:
        model = Kennel
        form = KennelFilterForm
        fields = [
            'name',
        ]
        filter_overrides = {
            CharField: {
                'filter_class': CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }
