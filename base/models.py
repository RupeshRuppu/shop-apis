from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class MasterProducts(models.Model):
    gender_choice = [("M", "MALE"), ("F", "FEMALE"), ("K", "KIDS")]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=500, null=False)
    price = models.FloatField(null=False)
    rating = models.FloatField(null=False)
    product_description = models.TextField(null=False)
    reviews = models.TextField(null=False)
    reviews_rating = models.TextField(null=False)
    url = models.TextField(null=False)
    size = models.FloatField(null=False)
    color = models.CharField(max_length=50, null=False)
    category = models.CharField(max_length=50, null=False)
    gender = models.CharField(
        max_length=10, null=True, blank=True, choices=gender_choice
    )

    class Meta:
        db_table = "master_products"

    def __str__(self) -> str:
        return f"{self.title},{self.id}"


class UserCart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    dateCreated = models.DateTimeField(default=datetime.now)
    product = models.ForeignKey(MasterProducts, on_delete=models.CASCADE)
    count = models.IntegerField(default=1, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "cart"

    def __str__(self) -> str:
        return f"{self.product.id} {self.user.username}"


class UserOrders(models.Model):
    order_status_choices = [
        ("PICKED", "PICKED"),
        ("DISPATCHED", "DISPATCHED"),
        ("DELIVERED", "DELIVERED"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    dateCreated = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_ids = models.CharField(max_length=2000, null=False, blank=False)
    order_status = models.CharField(
        max_length=10,
        choices=order_status_choices,
        default="PICKED",
    )
    order_total = models.FloatField(null=False, blank=False)

    class Meta:
        db_table = "orders"

    def __str__(self) -> str:
        return f"{self.id} {self.user.username} {self.order_status}"
