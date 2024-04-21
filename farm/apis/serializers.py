from rest_framework import serializers
from farm.models import Income, Expense, Farm, Poultry


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = "__all__"


class PoultrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Poultry
        fields = "__all__"
