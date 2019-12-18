from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Good


class GoodSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Good
        fields = ('id', 'good_name', 'good_price', 'owner')


class UserSerializer(serializers.ModelSerializer):
    goods = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Good.objects.all())

    class Meta:
        model = Good
        fields = ('id', 'username', 'goods')
