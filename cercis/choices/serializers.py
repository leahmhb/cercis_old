from rest_framework.serializers import CurrentUserDefault, HiddenField, ModelSerializer

from .models import Color, Country, Title


class TitleSerializer(ModelSerializer):
    lookup_field = "id"
    read_only_fields = ['id', 'created_by']
    created_by = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Title
        fields = "__all__"


class ColorSerializer(ModelSerializer):
    lookup_field = "id"
    read_only_fields = ['id', 'created_by']
    created_by = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Color
        fields = "__all__"


class CountrySerializer(ModelSerializer):
    lookup_field = "id"
    read_only_fields = ['id', 'created_by']
    created_by = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Country
        fields = "__all__"
