from django.contrib import admin
from products.models import Product, Category, CartItem, Order, OrderItem

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
