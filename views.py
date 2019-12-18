from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FormParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GoodSerializer 
from .models import Good

# Create your views here.
@api_view(['GET', 'POST'])
def good_list(request, format=None):
  if request.method == 'GET':
    goods = Good.objects.all()
    serializer = GoodSerializer(goods, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = GoodSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def good_detail(request, pk, format=None):
  try:
    good = Good.objects.get(pk=pk)
  except Exception:
    return Response(status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    s = GoodSerializer(good)
    return Response(s.data)
  elif request.method == 'PUT':
    data = FormParser().parse(request)
    s = GoodSerializer(good, data=data)
    if s.is_valid():
      s.save()
      return Response(s.data)
    return Response(s.errors, status=status.HTTP_404_NOT_FOUND)
  elif request.method == 'DELETE':
    good.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)