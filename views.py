from rest_framework import generics
from .models import Good
from .serializers import GoodSerializer

# Create your views here.
class GoodList(generics.ListCreateAPIView):
  queryset = Good.objects.all()
  serializer_class = GoodSerializer


class GoodDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Good.objects.all()
  serializer_class = GoodSerializer