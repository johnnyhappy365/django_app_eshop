from rest_framework import generics
from rest_framework import permissions
from .models import Good, GoodCategory
from .serializers import GoodSerializer, GoodCategorySerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import viewsets


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

