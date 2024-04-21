from datetime import datetime
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from mpesa.apis.serializers import LNMOnlineSerializer
from mpesa.models import LNMOnline


class LNMOnlineCreateAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        print(request.data)
        body = request.data.get("Body", {}).get("stkCallback", {})
        merchant_request_id = body.get("MerchantRequestID")
        checkout_request_id = body.get("CheckoutRequestID")
        result_code = body.get("ResultCode")
        result_desc = body.get("ResultDesc")
        callback_metadata = body.get("CallbackMetadata", {}).get("Item", [])
        amount = callback_metadata[0].get("Value", "")
        mpesa_receipt_number = callback_metadata[1].get("Value", "")
        phone_number = callback_metadata[4].get("Value", "")
        transaction_date = callback_metadata[3].get("Value", "")
        str_transaction_date = str(transaction_date)
        transaction_datetime = datetime.strptime(str_transaction_date, "%Y%m%d%H%M%S")

        transaction_model = LNMOnline.objects.create(
            MerchantRequestID=merchant_request_id,
            CheckoutRequestID=checkout_request_id,
            ResultCode=result_code,
            ResultDesc=result_desc,
            Amount=amount,
            MpesaReceiptNumber=mpesa_receipt_number,
            TransactionDate=transaction_datetime,
            PhoneNumber=phone_number,
        )

        transaction_model.save()

        return Response(
            {"result descripition": "The service request is processed successfully."}
        )
