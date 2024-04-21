from django.db import models
from products.models import Order


class LNMOnline(models.Model):
    MerchantRequestID = models.CharField(max_length=60)
    CheckoutRequestID = models.CharField(max_length=60)
    ResultCode = models.IntegerField()
    ResultDesc = models.CharField(max_length=150)
    Amount = models.FloatField()
    MpesaReceiptNumber = models.CharField(max_length=20)
    TransactionDate = models.DateTimeField()
    PhoneNumber = models.CharField(max_length=15)
    order = models.ForeignKey(
        Order, related_name="lnm_payments", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"LNMOnline Payment - {self.MpesaReceiptNumber}"
