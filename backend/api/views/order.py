from rest_framework.viewsets import ModelViewSet
from api.models.order import Order
from api.serializers.order import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "uuid"
