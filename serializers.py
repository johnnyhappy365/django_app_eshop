from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Good, GoodCategory


class GoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodCategory
        fields = ("id", "name", "parent")


class GoodSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    category = GoodCategorySerializer(read_only=True)

    class Meta:
        model = Good
        fields = ("id", "good_name", "good_price", "owner", "category")


class UserSerializer(serializers.ModelSerializer):
    goods = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Good.objects.all()
    )

    class Meta:
        model = Good
        fields = ("id", "username", "goods")


class GoodStatSerializer(serializers.Serializer):
    def to_representation(self, obj):
        return obj

