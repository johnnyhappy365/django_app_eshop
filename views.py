from rest_framework import generics
from rest_framework import permissions
from .models import Good, GoodCategory
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, mixins, generics
from django.db.models import Count
from django.db.models.functions import (
    TruncDay,
    TruncHour,
    TruncWeek,
    TruncMonth,
    TruncYear,
)
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

    # 在API页面中看不到freq, 因为不适合加到上面。这个字段的作用是作为query参数，而不是过滤参数。一但变成过滤参数就会在sql中使用到这个参数
    class Meta:
        model = Good
        fields = (
            "good_name",
            "good_price",
            "category__name",
            "created_at",
            # "freq",
        )


class GoodHistStatViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = GoodStatSerializer
    filter_class = GoodHistStatFilter

    def get_queryset(self):
        # 默认按天粒度统计
        freq = self.request.query_params.get("freq", "day")
        # 按不同时间粒度进行聚合
        trunc_freqs = {
            "day": TruncDay,
            "hour": TruncHour,
            "week": TruncWeek,
            "month": TruncMonth,
            "year": TruncYear,
        }
        trunc_method = trunc_freqs[freq]
        return (
            Good.objects.annotate(date=trunc_method("created_at"))
            .values("date")
            .annotate(count=Count("id"))
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

