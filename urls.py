from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"goods", views.GoodViewSet)
urlpatterns = [
    url(r"^", include(router.urls)),
    url(
        r"^api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
]
