from django.urls import path
from old_day_chicks.apis.views import (
    DayOldChicksOrderListAPIView,
    DayOldChicksOrderDetailsAPIView,
)

urlpatterns = [
    path("orders/", DayOldChicksOrderListAPIView.as_view()),
    path("orders/<str:pk>/", DayOldChicksOrderDetailsAPIView.as_view()),
]
