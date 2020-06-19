from django.contrib import admin

from .models import Color, Country, Title


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "code",
        "text",
        "is_active",
    )
    list_display_links = ("code", "text")
    list_filter = ("is_active",)
    list_editable = ("is_active",)
    search_fields = ("code", "text")
    list_per_page = 25


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "text",
        "is_active",
    )
    list_display_links = ("text",)
    list_filter = ("is_active",)
    list_editable = ("is_active",)
    search_fields = ("text",)
    list_per_page = 25


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "abbr",
        "full",
        "sport",
        "kennel_club",
        "is_active",
    )
    list_display_links = ("abbr",)
    list_filter = ("is_active", "sport")
    list_editable = ("is_active",)
    search_fields = ("abbr",)
    list_per_page = 25
