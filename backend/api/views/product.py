from rest_framework.viewsets import ModelViewSet
from api.models.product import Product
from api.serializers.product import ProductSerializer, ProductDetailSerializer
from rest_framework.response import Response
from rest_framework import status


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "uuid"

    def create(self, request, *args, **kwargs):
        print(f"Recibiendo nuevo producto: {request.data.get('product')}")

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(f"Actualizando producto con UUID: {instance.uuid}")

        serializer = self.get_serializer(
            instance, data=request.data, partial=kwargs.get("partial", False)
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
