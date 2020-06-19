import csv

from django.contrib.admin import ModelAdmin, TabularInline, register, site
from django.http import HttpResponse

from .models import Image, Kennel, Person, Poodle, HealthClearance


def export_poodles(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="books.csv"'
    writer = csv.writer(response)
    poodles = Poodle.objects.all().values_list()
    columns = Poodle.objects.values().first().keys()
    writer.writerow(columns)
    for p in poodles:
        writer.writerow(p)
    return response


export_poodles.short_description = "Export to csv"


class image_inline(TabularInline):
    model = Image
    extra = 1
    max_num = 12


class healthclearance_inline(TabularInline):
    model = HealthClearance
    extra = 1
    max_num = 12


@register(Poodle)
class PoodleAdmin(ModelAdmin):
    raw_id_fields = (
                     'owners',
                     'breeders',
                     'origin_country',
                     'color',
                     'sire',
                     'dam',
                     'titles_prefix',
                     'titles_suffix'
                    )

    autocomplete_lookup_fields = {
        'fk': ['sire',
               'dam',
               'origin_country',
               'color', ],
        'm2m': ['owners', 'breeders', 'titles_prefix', 'titles_suffix'],
    }

    inlines = [image_inline, healthclearance_inline]
    list_display = (
        "created_at",
        "id",
        "name_registered",
        "sex",
        "color",
        "pd_color",
        "variety",
        "origin_country",
        "is_viewable",
    )
    list_display_links = ("name_registered",)
    list_filter = ("is_viewable", "sex", "color", "origin_country")
    list_editable = (
        "is_viewable",
    )
    search_fields = (
        'name_registered',
        'color__text',
        'origin_country__text',
        'breeders__full_name',
        'owners__full_name',
        'sire__name_registered',
        'dam__name_registered',
        'titles_prefix__abbr',
        'titles_suffix__abbr'
    )
    list_per_page = 25
    actions = [export_poodles]
    list_select_related = (
        'color',
        'origin_country'
    )
    readonly_fields = ["pd_id", "pd_variety", "pd_color", "pd_owner", "pd_breeder", 'dob_dod']
    basic_fields = (
        'is_viewable',
        'name_registered',
        'name_call', 'origin_country',
        'sex', 'height',
        'honorifics',
        ('titles_prefix', 'titles_suffix'),
        'akc', 'ukc',
        'addtl',
        ('pd_color', 'color'),
        'variety',
        'dob_dod',
        ('dob', 'dod'),
        ('owners', 'breeders'),
        'sire', 'dam'
    )

    fieldsets = (
        (None, {
            'classes': (),
            'fields': basic_fields
        }),
        ('Health', {
            'classes': ('collapse',),
            'fields': (
                'chic', 'health_information',
                'hip_clearance',
                'vwd_clearance',
                'eye_clearance',
                'sa_clearance',
                'heart_clearance',
                'elbow_clearance',
                'patella_clearance',
                'thyroid_clearance',
                'legg_c_p_clearance',
                'pra_optigen_clearance',
                'neonatal_enceph_clearance'
                ),
        }),
    )

    show_full_result_count = False

    def get_queryset(self, request):
        qs = super(PoodleAdmin, self).get_queryset(request)
        return qs.select_related(
            "color", "origin_country",
            "sire", "dam",
        ).prefetch_related(
            "color", "origin_country",
            "sire", "dam",
            "owners", "breeders"
        )


@register(Image)
class ImageAdmin(ModelAdmin):
    list_display = (
        "caption",
        "poodle",
        "comments",
        "is_viewable",
    )
    list_display_links = ("caption", "poodle")
    list_editable = ("is_viewable",)
    search_fields = ("caption", "poodle", "category", "comments")
    list_per_page = 25


@register(HealthClearance)
class HealthClearanceAdmin(ModelAdmin):
    list_display = ('name', 'result', 'poodle', 'is_viewable', )
    list_display_links = ('name', 'result', 'poodle')
    list_filter = ('name', 'result', )
    list_editable = ('is_viewable',)
    search_fields = ('name', 'result', 'poodle')
    list_per_page = 25


class people_inline(TabularInline):
    model = Person
    extra = 1
    max_num = 4


@register(Person)
class PersonAdmin(ModelAdmin):
    autocomplete_fields = ['country', 'kennel']
    list_display = (
        "id",
        "full_name",
        "kennel",
        "country",
        "is_viewable",
    )
    list_display_links = ("full_name", )
    list_filter = ("is_viewable", "kennel", )
    list_editable = ("is_viewable", "kennel")
    search_fields = ["full_name", ]
    list_select_related = (
        'country'
    )
    list_per_page = 25
    show_full_result_count = False
    list_select_related = ("kennel", )


@register(Kennel)
class KennelAdmin(ModelAdmin):
    inlines = [people_inline]
    list_display = (
        "name",
        "is_viewable",
    )
    list_display_links = ("name",)
    list_filter = ("is_viewable",)
    list_editable = ("is_viewable",)
    search_fields = ("is_viewable", "name",)
    list_per_page = 25
    show_full_result_count = False
