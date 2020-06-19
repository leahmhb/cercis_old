# Generated by Django 3.0.5 on 2020-05-29 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('choices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kennel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from=['name'], unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('is_viewable', models.BooleanField(default=True, verbose_name='Viewable?')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
            options={
                'verbose_name_plural': 'Kennels',
                'ordering': ['name', 'id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from=['full_name', 'id', 'created_at'], unique=True)),
                ('full_name', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Full Name')),
                ('pd_kennel', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Kennel on PD')),
                ('web_url', models.URLField(blank=True, default='', max_length=300, null=True, verbose_name='Website')),
                ('fb_url', models.URLField(blank=True, default='', max_length=300, null=True, verbose_name='Facebook')),
                ('is_viewable', models.BooleanField(default=True, verbose_name='Viewable?')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='choices.Country', verbose_name='Country')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('kennel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='person_kennel', to='core.Kennel', verbose_name='Kennel')),
            ],
            options={
                'verbose_name_plural': 'People',
                'ordering': ['full_name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Poodle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, default=None, editable=False, populate_from='name_registered', unique=True)),
                ('pd_id', models.IntegerField(null=True, unique=True, verbose_name='PD ID')),
                ('name_call', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Call Name')),
                ('name_registered', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Registered Name')),
                ('pd_owner', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='PD Owner')),
                ('pd_breeder', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='PD Breeder')),
                ('honorifics', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Honorifics')),
                ('chic', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='CHIC')),
                ('akc', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='AKC')),
                ('akc_dna', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='AKC DNA')),
                ('ukc', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='UKC')),
                ('addtl', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Addtl Reg')),
                ('sex', models.CharField(choices=[('M', 'Dog'), ('F', 'Bitch'), ('U', 'Unknown')], max_length=1, verbose_name='Sex')),
                ('pd_color', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='PD Color')),
                ('height', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Height')),
                ('dob_dod', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Lifespan')),
                ('dob', models.CharField(blank=True, max_length=12, null=True, verbose_name='Date of Birth')),
                ('dod', models.CharField(blank=True, max_length=12, null=True, verbose_name='Date of Death')),
                ('pedigree_src', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Pedigree Source')),
                ('variety', models.CharField(blank=True, choices=[('S', 'Standard'), ('M', 'Miniature/Moyen'), ('D', 'Dwarf'), ('T', 'Toy')], default='', max_length=1, null=True, verbose_name='Variety')),
                ('pd_variety', models.CharField(blank=True, default='', max_length=1, null=True, verbose_name='PD Variety')),
                ('vwd_clearance', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Von Willebrand Disease')),
                ('thyroid_clearance', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Thyroid')),
                ('legg_c_p_clearance', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Legg-Calvé-Perthes Disease (LCP)')),
                ('pra_optigen_clearance', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Progressive Retinal Atrophy (PRA)')),
                ('neonatal_enceph_clearance', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Neonatal Encephalopathy')),
                ('hip_clearance', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Hip Dysplasia')),
                ('eye_clearance', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Eye Examination')),
                ('sa_clearance', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Sebaceous Adenitis (SA)')),
                ('heart_clearance', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Cardiac Disease')),
                ('elbow_clearance', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Elbow Dysplasia')),
                ('patella_clearance', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Patellar Luxation')),
                ('health_information', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Other Health Info')),
                ('comments', models.TextField(blank=True, default='', null=True, verbose_name='Comments')),
                ('is_viewable', models.BooleanField(default=False, verbose_name='Viewable?')),
                ('breeders', models.ManyToManyField(blank=True, related_name='bred_poodles', to='core.Person', verbose_name='Breeder(s)')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='choices.Color', verbose_name='Color')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('dam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='poodle_dam', to='core.Poodle', verbose_name='Dam')),
                ('origin_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='choices.Country', verbose_name='Country')),
                ('owners', models.ManyToManyField(blank=True, related_name='owns_poodles', to='core.Person', verbose_name='Owner(s)')),
                ('sire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='poodle_sire', to='core.Poodle', verbose_name='Sire')),
            ],
            options={
                'verbose_name_plural': 'Poodles',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from=['poodle__name_call', 'caption', 'id'], unique=True)),
                ('path', models.ImageField(upload_to='images/')),
                ('caption', models.CharField(default='caption', max_length=255)),
                ('comments', models.TextField(blank=True, default='', null=True, verbose_name='Comments')),
                ('is_viewable', models.BooleanField(default=False, verbose_name='Viewable?')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('poodle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='poodles_images', to='core.Poodle', verbose_name='Poodle')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'abstract': False,
            },
        ),
    ]
