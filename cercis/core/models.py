from choices.models import Color, Country, Title
from django.db.models import (
    PROTECT,
    SET_NULL,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    ImageField,
    IntegerField,
    ManyToManyField,
    Model,
    Q,
    TextField,
    URLField,
)
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField

NULL_AND_BLANK = {'null': True, 'blank': True}

SEX_CHOICES = (
    ("M", "Dog"),
    ("F", "Bitch"),
    ("U", "Unknown"),
)

VARIETY_CHOICES = (("S", "Standard"), ("M", "Miniature/Moyen"), ("D", "Dwarf"), ("T", "Toy"))


class BaseModel(Model):
    created_at = DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = DateTimeField(verbose_name="Updated", auto_now=True)
    created_by = ForeignKey('users.User', verbose_name="Creator", on_delete=SET_NULL, **NULL_AND_BLANK)

    class Meta:
        abstract = True
        app_label = 'core'


class Kennel(BaseModel):
    slug = AutoSlugField(
        null=True,
        default=None,
        unique=True,
        populate_from=["name"],
    )
    name = CharField(verbose_name="Name", max_length=50)
    is_viewable = BooleanField(verbose_name="Viewable?", default=True)

    class Meta(BaseModel.Meta):
        verbose_name_plural = "Kennels"
        ordering = ["name", "id"]

    def __str__(self):
        return self.name

    def people(self):
        return self.person_kennel.all()

    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains",)


class Person(BaseModel):
    slug = AutoSlugField(
        null=True,
        default=None,
        unique=True,
        populate_from=["full_name", "id", "created_at"],
    )
    full_name = CharField(verbose_name="Full Name", max_length=200, **NULL_AND_BLANK, default='')
    pd_kennel = CharField(
        verbose_name="Kennel on PD",
        max_length=100,
        blank=True,
        null=True,
        default=""
    )
    kennel = ForeignKey(
        Kennel,
        verbose_name="Kennel",
        related_name="person_kennel",
        on_delete=PROTECT,
        null=True,
        blank=True,
    )
    country = ForeignKey(
        Country, verbose_name="Country", on_delete=PROTECT, **NULL_AND_BLANK
    )
    web_url = URLField(verbose_name="Website", max_length=300, **NULL_AND_BLANK, default="")
    fb_url = URLField(verbose_name="Facebook", max_length=300, **NULL_AND_BLANK, default="")
    is_viewable = BooleanField(verbose_name="Viewable?", default=True)

    class Meta(BaseModel.Meta):
        verbose_name_plural = "People"
        ordering = ["full_name"]

    def __str__(self):
        return "{}".format(self.full_name)

    def get_absolute_url(self):
        return reverse("core:person-detail", args=[str(self.slug)])

    @staticmethod
    def autocomplete_search_fields():
        return ('full_name__icontains',)


class Poodle(BaseModel):
    slug = AutoSlugField(default=None, unique=True, populate_from="name_registered")
    pd_id = IntegerField(verbose_name="PD ID", unique=True, null=True)
    name_call = CharField(verbose_name="Call Name", max_length=50, blank=True,
                          null=True,
                          default="")
    name_registered = CharField(
        verbose_name="Registered Name",
        max_length=500,
        blank=True,
        null=True,
        default="",
    )
    owners = ManyToManyField(
        Person, verbose_name="Owner(s)",
        related_name="owns_poodles",
        blank=True
    )
    breeders = ManyToManyField(
        Person, verbose_name="Breeder(s)",
        related_name="bred_poodles",
        blank=True
    )
    pd_owner = CharField(
        verbose_name="PD Owner",
        max_length=200,
        null=True,
        blank=True,
        default=""
    )
    pd_breeder = CharField(
        verbose_name="PD Breeder",
        max_length=200,
        null=True,
        blank=True,
        default=""
    )
    origin_country = ForeignKey(
        Country, verbose_name="Country",
        on_delete=PROTECT,
        null=True
    )
    honorifics = CharField(verbose_name="Honorifics", max_length=50, blank=True, null=True, default="")
    chic = CharField(
        verbose_name="CHIC",
        max_length=50,
        null=True,
        blank=True,
        default=""
    )
    akc = CharField(
        verbose_name="AKC",
        max_length=50,
        null=True,
        blank=True,
        default=""
    )
    akc_dna = CharField(
        verbose_name="AKC DNA", max_length=50, **NULL_AND_BLANK, default=""
    )
    ukc = CharField(
        verbose_name="UKC", max_length=50, **NULL_AND_BLANK, default=""
    )
    addtl = CharField(
        verbose_name="Addtl Reg",
        max_length=50,
        null=True,
        blank=True,
        default="",
    )
    sex = CharField(verbose_name="Sex", max_length=1, choices=SEX_CHOICES)
    pd_color = CharField(
        verbose_name="PD Color",
        max_length=100,
        blank=True,
        null=True,
        default=""
    )
    height = CharField(verbose_name="Height", max_length=10, blank=True, null=True, default="")
    color = ForeignKey(Color, verbose_name="Color", on_delete=PROTECT, null=True)
    dob_dod = CharField(verbose_name="Lifespan", max_length=60, blank=True, null=True, default="")
    dob = CharField(verbose_name="Date of Birth", max_length=12, blank=True, null=True)
    dod = CharField(verbose_name="Date of Death", max_length=12, blank=True, null=True)
    sire = ForeignKey(
        "self",
        verbose_name="Sire",
        related_name="poodle_sire",
        null=True,
        on_delete=PROTECT
    )
    dam = ForeignKey(
        "self",
        verbose_name="Dam",
        related_name="poodle_dam",
        null=True,
        on_delete=PROTECT
    )
    pedigree_src = CharField(
        verbose_name="Pedigree Source",
        max_length=100,
        null=True,
        blank=True,
        default=""
    )
    variety = CharField(
        verbose_name="Variety",
        max_length=1,
        null=True,
        blank=True,
        default="",
        choices=VARIETY_CHOICES
    )
    pd_variety = CharField(
        verbose_name="PD Variety",
        max_length=1,
        null=True,
        blank=True,
        default="",
    )
    titles_prefix = ManyToManyField(
        Title,
        verbose_name="Prefix Titles",
        related_name="poodles_prefix",
        blank=True)
    titles_suffix = ManyToManyField(
        Title,
        verbose_name="Suffix Titles",
        related_name="poodles_suffix",
        blank=True)
    vwd_clearance = CharField(verbose_name="Von Willebrand Disease", max_length=100, blank=True, null=True, default="")
    thyroid_clearance = CharField(verbose_name="Thyroid", max_length=100, blank=True, null=True, default="")
    legg_c_p_clearance = CharField(verbose_name="Legg-Calvé-Perthes Disease (LCP)",
                                   max_length=100, blank=True, null=True, default="")
    pra_optigen_clearance = CharField(
        verbose_name="Progressive Retinal Atrophy (PRA)", max_length=100, blank=True, null=True, default=""
    )
    neonatal_enceph_clearance = CharField(
        verbose_name="Neonatal Encephalopathy", max_length=100, blank=True, null=True, default=""
    )
    hip_clearance = CharField(verbose_name="Hip Dysplasia", max_length=100, blank=True, null=True, default="")
    eye_clearance = CharField(verbose_name="Eye Examination", max_length=100, blank=True, null=True, default="")
    sa_clearance = CharField(verbose_name="Sebaceous Adenitis (SA)", max_length=100, blank=True, null=True, default="")
    heart_clearance = CharField(verbose_name="Cardiac Disease", max_length=100, blank=True, null=True, default="")
    elbow_clearance = CharField(verbose_name="Elbow Dysplasia", max_length=100, blank=True, null=True, default="")
    patella_clearance = CharField(verbose_name="Patellar Luxation", max_length=100, blank=True, null=True, default="")
    health_information = CharField(verbose_name="Other Health Info", max_length=100, blank=True, null=True, default="")
    comments = TextField(verbose_name="Comments", **NULL_AND_BLANK, default="")
    is_viewable = BooleanField(verbose_name="Viewable?", default=False)

    class Meta(BaseModel.Meta):
        verbose_name_plural = "Poodles"

    def __str__(self):
        if self.name_call:
            return '{n} "{c}"'.format(n=self.name_registered, c=self.name_call)
        else:
            return self.name_registered

    def get_absolute_url(self):
        return reverse("core:poodle-detail", args=[str(self.slug)])

    def offspring(self):
        return Poodle.objects.filter(
            Q(sire=self.id) | Q(dam=self.id)
            ).order_by(
                'sire', 'dam'
            ).select_related(
                "color", "origin_country",
                "sire", "dam",
            ).prefetch_related(
                "color", "origin_country",
                "sire", "dam",
            )

    def siblings_full(self):
        return Poodle.objects.filter(
            Q(sire=self.sire) & Q(dam=self.dam)
        ).order_by(
            'name_registered'
        )

    def siblings_damside(self):
        return Poodle.objects.filter(
                ~ Q(sire=self.sire) & Q(dam=self.dam)
            ).order_by(
                'dam'
            )

    def siblings_sireside(self):
        return Poodle.objects.filter(
            Q(sire=self.sire) & ~Q(dam=self.dam)
        ).order_by(
            'sire'
        )

    def images(self):
        return self.poodles_images.all()

    @staticmethod
    def autocomplete_search_fields():
        return ('name_registered__icontains', 'name_call__icontains')


class HealthClearance(Model):
    poodle = ForeignKey(Poodle, verbose_name="Poodle",
                        related_name='poodles_health',
                        on_delete=PROTECT)
    name = CharField(verbose_name="Clearance", max_length=255, **NULL_AND_BLANK)
    result = CharField(verbose_name="Result", max_length=50,
                       **NULL_AND_BLANK)
    ofa_num = CharField(verbose_name="OFA #", max_length=50, **NULL_AND_BLANK)
    is_viewable = BooleanField(verbose_name="Viewable?", default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s: %s' % (self.poodle.name_call, self.name, self.result)


class Image(BaseModel):
    slug = AutoSlugField(
        null=True,
        default=None,
        unique=True,
        populate_from=["poodle__name_call", "caption", "id"],
    )
    poodle = ForeignKey(
        Poodle, verbose_name="Poodle", related_name="poodles_images", on_delete=PROTECT
    )
    path = ImageField(upload_to="images/")
    caption = CharField(max_length=255, default="caption")
    comments = TextField(verbose_name="Comments", **NULL_AND_BLANK, default="")
    is_viewable = BooleanField(verbose_name="Viewable?", default=False)

    def __str__(self):
        return "%s %s" % (self.poodle.name_call, self.caption)

    class Meta(BaseModel.Meta):
        verbose_name_plural = "Images"
