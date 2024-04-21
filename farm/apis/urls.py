from django.urls import path
from farm.apis.views import (
    IncomeListCreateAPIView,
    IncomeDetailsAPIView,
    ExpenseListCreateAPIView,
    ExpenseDetailsAPIView,
    farmListCreateAPIView,
    farmDetailsAPIView,
    PoultryListCreateAPIView,
    PoultryDetailsAPIView,
)

urlpatterns = [
    path("incomes/", IncomeListCreateAPIView.as_view(), name="income-list"),
    path("incomes/<str:pk>/", IncomeDetailsAPIView.as_view(), name="income-list"),
    path("expense/", ExpenseListCreateAPIView.as_view(), name="expense-list"),
    path("expense/<str:pk>/", ExpenseDetailsAPIView.as_view(), name="expense-details"),
    path("", farmListCreateAPIView.as_view(), name="farm"),
    path("<str:pk>/", farmDetailsAPIView.as_view(), name="farm-details"),
    path("poultrys-details/", PoultryListCreateAPIView.as_view(), name="poultry"),
    path("poultrys-details/<str:pk>/", PoultryDetailsAPIView.as_view(), name="details"),
]
