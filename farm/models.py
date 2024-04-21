from django.db import models
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User


class Farm(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    farm_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    establishment_date = models.DateField()
    contact_person = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.farm_name

    class Meta:
        ordering = ["establishment_date"]


class Poultry(models.Model):
    BREED_CHOICES = [
        ("Kenbro", "Kenbro"),
        ("Broiler", "Broiler"),
        ("Layers", "Layers"),
    ]

    age_in_weeks = models.PositiveIntegerField()
    no_of_poultries = models.PositiveIntegerField()
    breed = models.CharField(max_length=50, choices=BREED_CHOICES)
    date_add = models.DateField(auto_now_add=True)
    description = models.TextField(default=True)

    def __str__(self):
        return self.breed

    class Meta:
        ordering = ["date_add"]


class Income(models.Model):
    SOURCE_CHOICES = [
        ("eggs", "Eggs"),
        ("chickens", "Chickens"),
        ("manure", "Manure"),
        ("other", "Other Poultry Products"),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    sale_date = models.DateField()
    quantity = models.CharField(max_length=50)
    amount_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.source} {self.sale_date}"

    def save(self, *args, **kwargs):
        numeric_quantity = self._parse_quantity(self.quantity)
        numeric_quantity_decimal = Decimal(str(numeric_quantity))
        self.total_amount = self.amount_per_item * numeric_quantity_decimal
        super().save(*args, **kwargs)

    def _parse_quantity(self, quantity_str):
        try:
            return float(quantity_str.split()[0])
        except ValueError:
            return 0


class Expense(models.Model):
    ITEM_CHOICES = [
        ("drugs", "Drugs"),
        ("feeding_brooders", "Feeding Brooders"),
        ("feeds", "Feeds"),
        ("labour", "Labour"),
        ("maintenance_costs", "Maintenance Costs"),
        ("equipment", "Poultry Farm Equipment"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    item = models.CharField(max_length=100, choices=ITEM_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
