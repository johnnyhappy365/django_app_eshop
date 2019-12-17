from rest_framework import serializers
from .models import Good

class GoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Good
    fields = ('id', 'good_name', 'good_price')