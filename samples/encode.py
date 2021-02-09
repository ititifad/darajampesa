import base64
import keys

def generate_password(formatted_time):
    
    data_to_encode = keys.business_shortCode + keys.lipa_na_mpesa_passkey + formatted_time
    encoded = base64.b64encode(data_to_encode.encode())
    #print(encoded) b'MjAyMTAyMDgxOTAzMTg='

    decoded_password = encoded.decode('utf-8')
    
    return decoded_password
