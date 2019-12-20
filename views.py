from rest_framework import generics
from rest_framework import permissions
from .models import Good, GoodCategory
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, mixins, generics
from django.db.models import Count
from django.db.models.functions import TruncDay
import django_filters


class GoodViewSet(viewsets.ModelViewSet):
    #   此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    filter_fields = ("good_name", "good_price", "category__name")
    ordering_fields = ("good_name", "good_price")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.User)


class GoodHistStatFilter(django_filters.rest_framework.FilterSet):
    created_at = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Good
        fields = ("good_name", "good_price", "category__name", "created_at")


class GoodHistStatViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = GoodStatSerializer
    filter_class = GoodHistStatFilter

    def get_queryset(self):
        return (
            Good.objects.all()
            .annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(created_count=Count("id"))
            .order_by("date")
        )


class GoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = GoodCategory.objects.all()
    serializer_class = GoodCategorySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    filter_fields = ("name",)
    ordering_fields = ("name",)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.User)

