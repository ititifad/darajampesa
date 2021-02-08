import requests
from datetime import datetime
import keys
from requests.auth import HTTPBasicAuth
import base64


unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

data_to_encode = keys.business_shortCode + keys.lipa_na_mpesa_passkey + formatted_time
encoded = base64.b64encode(data_to_encode.encode())
#print(encoded) b'MjAyMTAyMDgxOTAzMTg='

decoded_password = encoded.decode('utf-8')
#print(decoded_password)
#print(formatted_time, "this is the formatted time")

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = (
    "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
)
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

json_response = r.json()  #{'access_token': 'sd0xlwWY9FlN48M0uaEGroI6Au91', 'expires_in': '3599'}

my_access_token = json_response['access_token']

def lipa_na_mpesa():
    
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    
    request = {
        "BusinessShortCode": keys.business_shortCode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_shortCode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://geitatech.herokuapp.com/nilipe",
        "AccountReference": "123456",
        "TransactionDesc": "Lipa kwa mpesa"
    }
    response = requests.post(api_url, json = request, headers=headers)
    print (response.text)
    
lipa_na_mpesa()