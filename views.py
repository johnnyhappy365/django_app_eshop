from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FormParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import GoodSerializer 
from .models import Good
# Create your views here.
def good_list(request):
  if request.method == 'GET':
    goods = Good.objects.all()
    serializer = GoodSerializer(goods, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def good_detail(request, pk):
  try:
    good = Good.objects.get(pk=pk)
  except Exception:
    return HttpResponse(404)
  if request.method == 'GET':
    s = GoodSerializer(good)
    return JsonResponse(s.data)
  elif request.method == 'PUT':
    data = FormParser().parse(request)
    s = GoodSerializer(good, data=data)
    if s.is_valid():
      s.save()
      return JsonResponse(s.data)
    return HttpResponse(s.errors, status=404)
  elif request.method == 'DELETE':
    good.delete()
    return HttpResponse(status=204)