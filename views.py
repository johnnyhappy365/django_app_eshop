from rest_framework import generics
from rest_framework import permissions
from .models import Good
from .serializers import GoodSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class GoodList(generics.ListCreateAPIView):
  queryset = Good.objects.all()
  serializer_class = GoodSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  def perform_create(self, serializer):
      serializer.save(owner=self.request.User)


class GoodDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Good.objects.all()
  serializer_class = GoodSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)