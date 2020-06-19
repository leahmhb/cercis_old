from choices.serializers import ColorSerializer, CountrySerializer
from rest_framework.reverse import reverse
from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
)

from .models import Image, Kennel, Person, Poodle


class KennelSerializer(ModelSerializer):
    lookup_field = "slug"
    url = SerializerMethodField()
    read_only_fields = ['id', 'created_by']
    created_by = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Kennel
        fields = "__all__"

    def get_url(self, ken):
        return reverse(
            "core:kennel-detail",
            kwargs=dict(slug=ken.slug),
            request=self.context["request"],
        )


class PersonSerializer(ModelSerializer):
    lookup_field = "slug"
    kennel = KennelSerializer()
    read_only_fields = ['id', 'created_by']
    created_by = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Person
        fields = ['id', 'kennel', 'pd_kennel', 'full_name', 'web_url', 'fb_url', 'created_by']
        read_only_fields = ['pd_kennel']


class PoodleBaseSerializer(ModelSerializer):
    lookup_field = "slug"
    url = SerializerMethodField()
    color_text = CharField(source='color.text', default='Unknown')
    origin_country_text = CharField(source='origin_country.text', default='Unknown')
    origin_country_code = CharField(source='origin_country.code', default='UNK')
    sire = CharField(source='sire.name_registered', default='--')
    dam = CharField(source='dam.name_registered', default='--')

    class Meta:
        model = Poodle
        fields = [
            'slug',
            'url', 'id', 'name_call', 'name_registered',
            'color_text', 'origin_country_code', 'sire', 'dam',
            'origin_country_text', 'dob', 'sex',
        ]
        read_only_fields = [
            'origin_country_code', 'origin_country_text', 'color_text',
            'dob_dod', 'sire', 'dam'
        ]

    def get_url(self, pood):
        """Return full API URL for serialized POST object"""
        return reverse(
            "core:poodle-detail",
            kwargs=dict(slug=pood.slug),
            request=self.context["request"],
        )


class PoodleFilterSerializer(PoodleBaseSerializer):
    owners = PersonSerializer(many=True)
    breeders = PersonSerializer(many=True)

    class Meta(PoodleBaseSerializer.Meta):
        model = Poodle
        fields = [
            'slug',
            'url', 'id', 'name_call', 'name_registered',
            'color_text', 'origin_country_code', 'sire', 'dam',
            'origin_country_text', 'dob', 'sex', 'owners', 'breeders'
        ]


class PoodleSerializer(ModelSerializer):
    lookup_field = "slug"
    url = SerializerMethodField()
    created_by = HiddenField(default=CurrentUserDefault())
    color = ColorSerializer()
    origin_country = CountrySerializer()
    owners = PersonSerializer(many=True)
    breeders = PersonSerializer(many=True)

    offspring = PoodleBaseSerializer(read_only=True, many=True)
    siblings_full = PoodleBaseSerializer(read_only=True, many=True)
    siblings_sireside = PoodleBaseSerializer(read_only=True, many=True)
    siblings_damside = PoodleBaseSerializer(read_only=True, many=True)

    class Meta:
        model = Poodle
        depth = 4
        exclude = ['pd_id']
        read_only_fields = [
            'pd_color', 'pd_variety', 'pd_owner',
            'pd_breeder', 'created_by',
            'origin_country_code', 'origin_country_text', 'color_text',
            'dob_dod',
        ]

    def get_url(self, pood):
        """Return full API URL for serialized POST object"""
        return reverse(
            "core:poodle-detail",
            kwargs=dict(slug=pood.slug),
            request=self.context["request"],
        )


class ImageSerializer(ModelSerializer):
    lookup_field = "slug"

    class Meta:
        model = Image
        fields = "__all__"
