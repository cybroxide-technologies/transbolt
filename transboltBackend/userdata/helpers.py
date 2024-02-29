import requests
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os


@csrf_exempt



def send_otp_to_phone(phone_number):
    smsApiKey = os.getenv("SMS_API_KEY")
    try:
        url = f'https://2factor.in/API/V1/{smsApiKey}/SMS/:{phone_number}/AUTOGEN3/:OTPtemp'
        response = requests.get(url)
        return HttpResponse(response , content_type='application/json')
    except Exception as e:
        return None
    


@csrf_exempt
def verify_otp_func(otp , phone_number):
    smsApiKey = os.getenv("SMS_API_KEY")
    try:
        print(smsApiKey)
        url = f'https://2factor.in/API/V1/{smsApiKey}/SMS/VERIFY3/:{phone_number}/{otp}'
        response = requests.get(url)
        return response.json() 
    
            
    except Exception as e:
        return str(e)
    




