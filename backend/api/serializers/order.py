from rest_framework import serializers
from api.models.order import Order
from api.models.order_item import OrderItem
from api.models.product import Product
from api.serializers.product import ProductOrderSerializer
from django.db import (
    transaction,
)  # for atomic transactions, or make all the order items created or none at all


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(
        queryset=Product.objects.all(), slug_field="uuid"
    )

    class Meta:
        model = OrderItem
        fields = ["product", "quantity"]

    def to_representation(self, instance: OrderItem):
        representation = super().to_representation(instance)
        representation["product"] = ProductOrderSerializer(instance.product).data
        return representation


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source="order_items")

    class Meta:
        model = Order
        fields = ["order_number", "items"]
        read_only_fields = ["order_number"]

    # Create One by One
    # def create(self, validated_data):
    #     # extract items info
    #     items_data = validated_data.pop("order_items")
    #     # create principal order without items
    #     order = Order.objects.create(**validated_data)
    #     # link items to the order
    #     for item_data in items_data:
    #         OrderItem.objects.create(order=order, **item_data)
    # 1 pedido que tiene 10 productos, 11 conexiones a la base de datos

    # return order

    # create bulk
    @transaction.atomic
    def create(self, validated_data):
        # extract items info
        items_data = validated_data.pop("items")
        # create principal order without items
        order = Order.objects.create(**validated_data)
        # link items to the order
        order_items = [OrderItem(order=order, **item_data) for item_data in items_data]
        OrderItem.objects.bulk_create(order_items)
        # 1 pedido que tiene 10 productos, 1 conexión a la base de datos, 1 query para crear la orden y 1 query para unir los items a la orden
        return order
