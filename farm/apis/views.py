from django.db.models import Q
from rest_framework import generics, permissions
from farm.models import Income, Expense, Farm, Poultry
from farm.apis.serializers import (
    IncomeSerializer,
    ExpenseSerializer,
    FarmSerializer,
    PoultrySerializer,
)


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is an admin
        if request.user.is_staff:
            return True
        # Check if the user is the owner of the farm
        return obj.user == request.user


class IncomeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = IncomeSerializer

    def get_queryset(self):
        user = self.request.user
        # If user is admin, return all orders, otherwise return orders of the user
        if user.is_staff:
            return Income.objects.all()
        return Income.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    permission_classes = [permissions.IsAuthenticated]


class IncomeDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsOwnerOrAdmin]


class ExpenseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user = self.request.user
        # If user is admin, return all orders, otherwise return orders of the user
        if user.is_staff:
            return Expense.objects.all()
        return Expense.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    permission_classes = [permissions.IsAuthenticated]


class ExpenseDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsOwnerOrAdmin]


class farmListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FarmSerializer

    def get_queryset(self):
        user = self.request.user
        # If user is admin, return all cartitems, otherwise return orders of the user
        if user.is_staff:
            return Farm.objects.all()
        return Farm.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    permission_classes = [permissions.IsAuthenticated]


class farmDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdmin]
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class PoultryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Poultry.objects.all()
    serializer_class = PoultrySerializer


class PoultryDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poultry.objects.all()
    serializer_class = PoultrySerializer
