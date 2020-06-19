from django.db.models import (
    SET_NULL,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    Model
)

NULL_AND_BLANK = {'null': True, 'blank': True}

KENNEL_CLUB_CHOICES = (
    ("AKC", "American Kennel Club"),
    ("UKC", "United Kennel Club"),
    ("CKC", "Canadian Kennel Club"),
    ("FCI", "Fédération Cynologique Internationale"),
    ("U", "Unknown")
)

SPORT_CHOICES = (
    ("C", "Conformation"),
    ("A", "Agility"),
    ("O", "Obedience"),
    ("P", "Performance"),
    ("U", "Unknown")
)


class BaseModel(Model):
    created_at = DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = DateTimeField(verbose_name="Updated", auto_now=True)
    created_by = ForeignKey('users.User', verbose_name="Creator", on_delete=SET_NULL, **NULL_AND_BLANK)

    class Meta:
        abstract = True
        app_label = 'choices'


class Country(BaseModel):
    code = CharField(unique=True, verbose_name="Code", max_length=3)
    text = CharField(verbose_name="Text", max_length=50)
    is_active = BooleanField(verbose_name="Active?", default=True)

    class Meta(BaseModel.Meta):
        verbose_name_plural = "Countries"
        ordering = ["code", "text"]

    def __str__(self):
        return "(%s) %s" % (self.code, self.text)

    @staticmethod
    def autocomplete_search_fields():
        return ('text__icontains', 'code__icontains')


class Color(BaseModel):
    text = CharField(verbose_name="Text", max_length=50)
    is_active = BooleanField(verbose_name="Active?", default=True)

    class Meta(BaseModel.Meta):
        verbose_name_plural = "colors"
        ordering = ["text"]

    def __str__(self):
        return "%s" % (self.text)

    @staticmethod
    def autocomplete_search_fields():
        return ('text__icontains',)


class Title(BaseModel):
    abbr = CharField(unique=True, verbose_name="Abbreviation", max_length=10)
    full = CharField(verbose_name="Full", max_length=200, **NULL_AND_BLANK)
    sport = CharField(verbose_name="Sport", max_length=50, choices=SPORT_CHOICES, **NULL_AND_BLANK)
    kennel_club = CharField(verbose_name="Kennel Club", choices=KENNEL_CLUB_CHOICES, max_length=4, **NULL_AND_BLANK)
    is_active = BooleanField(verbose_name="Active?", default=True)

    class Meta(BaseModel.Meta):
        verbose_name_plural = "Titles"
        ordering = ["abbr", "sport"]

    def __str__(self):
        return "%s" % (self.abbr)

    @staticmethod
    def autocomplete_search_fields():
        return ('abbr__icontains', 'sport__icontains')
