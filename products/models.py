from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    image_url = models.ImageField(upload_to="product_images/", null=True, blank=True)
    quantity = models.CharField(max_length=100)
    descriptions = models.TextField()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to="product_images/", null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} in {self.created_at}"

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.price
        super().save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    total_products_price = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="orderSummary", on_delete=models.CASCADE
    )
    product = models.IntegerField()
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name} {self.quantity} {self.price}"
