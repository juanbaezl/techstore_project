from rest_framework import serializers
from api.models.category import Category
from api.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="uuid"
    )

    class Meta:
        model = Product
        fields = ["product", "price", "zone", "category"]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="uuid"
    )

    class Meta:
        model = Product
        fields = "__all__"
