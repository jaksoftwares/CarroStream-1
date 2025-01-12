import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

from .credentials import MpesaAccessToken, LipanaMpesaPpassword




def token(request):
    consumer_key = 'FvFAsAmUt3KiVfuvAx0H2A8Lzg3VOS5IhyQ35ZgIBwdYVTW7'
    consumer_secret = 'CYycDezeZJ2X5tYLYcG4fF9bCiFFZPyycGJGppKEY0hVaMzW2gU6FJYFzaWOcJuy'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'payments/payment.html')



def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        
        request_data = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Carrostream Garage",
            "TransactionDesc": "Service Booking"
        }
        
        response = requests.post(api_url, json=request_data, headers=headers)

        # Check if the payment request was successful
        if response.status_code == 200:
            return render(request, 'dashboard/thank_you.html')  # Render the Thank You page
        else:
            return HttpResponse("Error processing payment", status=500)

