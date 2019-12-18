from rest_framework import generics
from rest_framework import permissions
from .models import Good
from .serializers import GoodSerializer
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
    filter_fields = ("good_name", "good_price")
    ordering_fields = ("good_name", "good_price")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.User)

