from django_filters import rest_framework as filters
from api.models.product import Product


class ProductFilter(filters.FilterSet):
    # Filter by product name
    product = filters.CharFilter(field_name="product", lookup_expr="icontains")

    # Filter by price range
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    # Filter by category UUID
    category = filters.UUIDFilter(field_name="category__uuid")

    # Filter by created at date
    created_at = filters.DateFromToRangeFilter(field_name="created_at")

    class Meta:
        model = Product
        fields = ["zone"]
