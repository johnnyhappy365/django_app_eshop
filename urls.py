from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  path(r'goods/', views.GoodList.as_view(), name='good_list'),
  path(r'goods/<int:pk>/', views.GoodDetail.as_view(), name='good_detail')
]

# 支持带后缀的请求，以响应不同的数据格式，如 goods.json goods.api等等
urlpatterns = format_suffix_patterns(urlpatterns)
