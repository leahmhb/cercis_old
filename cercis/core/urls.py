from core import views
from django.urls import include, path

app_name = "core"
urlpatterns = [
    path("vue-test/", views.VueTest.as_view(), name="vue-test"),
    path("poodles/", views.PoodleList.as_view(), name="poodles"),
    path('poodle/', include([
        path("detail/<str:slug>/", views.PoodleDetail.as_view(), name="poodle-detail"),
    ])),
    path('person/', include([
        path("detail/<str:slug>/", views.PersonDetail.as_view(), name="person-detail"),
    ])),
    path('kennel/', include([
        path("detail/<str:slug>/", views.KennelDetail.as_view(), name="kennel-detail"),
    ]))
]
