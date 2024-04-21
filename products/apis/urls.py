from django.urls import path
from products.apis.views import (
    ProductListCreateApiView,
    ProductDetailsApiView,
    CartItemListCreateApiView,
    CartItemDetailsApiView,
    CategoryListCreateApiView,
    CategoryDetailsApiView,
    OrderListCreateAPIView,
    OrderdetailsAPIView,
)

urlpatterns = [
    path("category/", CategoryListCreateApiView.as_view()),
    path("category/<int:pk>/", CategoryDetailsApiView.as_view()),
    path("products/", ProductListCreateApiView.as_view()),
    path("products/<int:pk>/", ProductDetailsApiView.as_view()),
    path("cartitems/", CartItemListCreateApiView.as_view()),
    path("cartitems/<int:pk>/", CartItemDetailsApiView.as_view()),
    path("orders/", OrderListCreateAPIView.as_view()),
    path("orders/<int:pk>/", OrderdetailsAPIView.as_view()),
]
