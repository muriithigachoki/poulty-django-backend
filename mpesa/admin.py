from django.contrib import admin
from mpesa.models import LNMOnline


class LNMOnlineAdmin(admin.ModelAdmin):
    list_display = (
        "MerchantRequestID",
        "CheckoutRequestID",
        "ResultCode",
        "ResultDesc",
        "Amount",
        "MpesaReceiptNumber",
        "TransactionDate",
        "PhoneNumber",
    )


admin.site.register(LNMOnline, LNMOnlineAdmin)
