from django.urls import path

from . import views

urlpatterns = [
  path(r'goods/', views.good_list, name='good_list'),
  path(r'goods/<int:pk>/', views.good_detail, name='good_detail')
]