from rest_framework import serializers
from api.models.category import Category
from api.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="uuid"
    )

    class Meta:
        model = Product
        fields = ["name", "price", "zone", "category"]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="uuid"
    )

    class Meta:
        model = Product
        fields = "__all__"


class ProductOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["uuid", "name", "price", "delivered"]

    def to_representation(self, instance: Product):
        representation = super().to_representation(instance)
        representation["category"] = instance.category.name if instance.category else ""
        return representation
