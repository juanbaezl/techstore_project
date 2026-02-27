from uuid import uuid4
from django.db import models

from api.models.product import Product


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_number = models.UUIDField(default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(Product, related_name="orders", through="OrderItem")
