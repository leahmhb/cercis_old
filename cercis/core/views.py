from django.contrib import messages
from django.views.generic import DetailView, TemplateView

from .models import Kennel, Person, Poodle


class VueTest(TemplateView):
    template_name = "vue-test.html"


class PoodleList(TemplateView):
    template_name = "core/poodle/all.html"


class PoodleDetail(TemplateView):
    template_name = "core/poodle/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = kwargs['slug']        
        return context


class PersonDetail(DetailView):
    model = Person
    queryset = Person.objects.select_related().prefetch_related()
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "person"
    template_name = "core/person/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.get_object().is_viewable:
            messages.add_message(
                self.request,
                messages.WARNING,
                """This person has not yet been approved by the admin team. Please wait for review.
                                        Your patience is appreciated! """
            )
        return context


class KennelDetail(DetailView):
    model = Kennel
    queryset = Kennel.objects.select_related().prefetch_related()
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "kennel"
    template_name = "core/kennel/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.get_object().is_viewable:
            messages.add_message(
                self.request,
                messages.WARNING,
                """This kennel has not yet been approved by the admin team. Please wait for review.
                                        Your patience is appreciated! """
            )
        return context
