from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from eshop import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"goods", views.GoodViewSet)
router.register(
    r"goodHistStat", views.GoodHistStatViewSet, basename="goodHistStat1"
)
router.register(r"goodCategories", views.GoodCategoryViewSet)
urlpatterns = [
    url(r"^", include(router.urls)),
    url(
        r"^api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
]
