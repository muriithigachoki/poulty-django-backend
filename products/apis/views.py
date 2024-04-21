from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from products.apis.serializers import (
    CartItemSerializer,
    OrderSerializer,
    ProductSerializers,
    CategorySerializers,
)
from products.models import Order, Product, CartItem, Category


class ProductListCreateApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductDetailsApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CategoryListCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetailsApiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.is_staff:
            return True
        # Check if the user is the owner of the order
        return obj.user == request.user


class CartItemListCreateApiView(ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        # If user is admin, return all cartitems, otherwise return orders of the user
        if user.is_staff:
            return CartItem.objects.all()
        return CartItem.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    permission_classes = [permissions.IsAuthenticated]


class CartItemDetailsApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdmin]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        # If user is admin, return all orders, otherwise return orders of the user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    permission_classes = [permissions.IsAuthenticated]


class OrderdetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdmin]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
