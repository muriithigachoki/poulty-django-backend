import base64

from payments import keys


def generate_password(formatted_time):
    data_to_encode = (
        keys.business_short_code + keys.lipa_na_mpesa_passkey + formatted_time
    )
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode("UTF-8")

    return decoded_password
