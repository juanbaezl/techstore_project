from uuid import uuid4
from django.db import models

from api.models.category import Category


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivered = models.BooleanField(default=False)
    zone = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # If the category is deleted, set the category of the product to NULL
        related_name="products",  # Allows: category.products.all()
        blank=True,
        null=True,
    )
