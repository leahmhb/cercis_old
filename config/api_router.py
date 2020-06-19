from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from choices.viewsets import ColorViewSet, CountryViewSet
from core.viewsets import (ImageViewSet, KennelViewSet, PersonViewSet,
                           PoodleFilterViewSet, PoodleViewSet)
from cercis.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

router.register(r"filter", PoodleFilterViewSet, basename="filter")

router.register(r"poodle", PoodleViewSet, basename="poodle")
router.register(r"image", ImageViewSet, basename="image")

router.register(r"person", PersonViewSet, basename="person")
router.register(r"kennel", KennelViewSet, basename="kennel")

router.register(r"color", ColorViewSet, basename="color")
router.register(r"country", CountryViewSet, basename="country")

app_name = "api"
urlpatterns = router.urls
