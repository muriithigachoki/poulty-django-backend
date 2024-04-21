from rest_framework import serializers
import requests
from products.models import Order, OrderItem, Product, CartItem, Category
from payments.access_token import register_access_token
from payments.encode import generate_password
from payments.date_formatting import formatted_time
from payments import keys

formatted_time = formatted_time()


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "user", "product", "name", "quantity", "price", "total_price"]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "product", "name", "quantity", "price", "total_price"]


def process_payment(phone_number, amount):
    access_token = register_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s" % access_token,
    }

    request = {
        "BusinessShortCode": keys.business_short_code,
        "Password": generate_password(formatted_time),
        "Timestamp": formatted_time,  # Use the formatted time string here
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": 174379,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://lit-beach-77859-33f6c1570728.herokuapp.com/api/payments/lnm/",
        "AccountReference": "Kangai Poultry Management system",
        "TransactionDesc": "Payment of one day chicks",
    }

    response = requests.post(api_url, json=request, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        result_code = response_data.get("resultCode")
        if result_code == "0":
            return True  # Payment successful
        else:
            return False  # Payment failed
    else:
        return False


# process_payment(254748522007, 1000)


class OrderSerializer(serializers.ModelSerializer):
    orderSummary = OrderItemSerializer(many=True, required=False)
    phone_number = serializers.CharField(max_length=15, required=False)
    amount = serializers.IntegerField(required=False)

    class Meta:
        model = Order
        fields = [
            "id",
            "name",
            "date",
            "address",
            "city",
            "total_products_price",
            "orderSummary",
            "phone_number",
            "amount",
        ]

    def create(self, validated_data):
        order_items_data = validated_data.pop("orderSummary", [])
        phone_number = validated_data.pop("phone_number", None)
        amount = validated_data.pop("amount", None)
        # process_payment(254748522007, amount)
        print(f"phone number: {phone_number}, Amount: {amount}")

        if amount is None and phone_number is None:
            raise ValueError(
                "Amount or phone_number is required when creating an order.", amount
            )

        order = Order.objects.create(amount=amount, **validated_data)

        if phone_number is not None and amount is not None:
            payment_processed = process_payment(phone_number, amount)
            print("Calling process_payment function...", phone_number, amount)

            if payment_processed:
                order.phone_number = phone_number
                order.amount_paid = amount
                order.save()

        for order_item_data in order_items_data:
            OrderItem.objects.create(order=order, **order_item_data)
        return order
