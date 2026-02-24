from rest_framework import serializers
from api.models.product import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["product", "price", "zone"]


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
