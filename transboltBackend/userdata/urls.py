from django.urls import path
from .views import *

urlpatterns = [
    path('send-otp/' , send_otp),
    path('verify-otp/' , verify_otp),
    path('sign-up/' , userSignUp),
    path('users/' , userdataorm),
    path('vehicle-sign-up/' , vehicleSignUp),
    path('vehicles/' , vehicledataorm),
    
    ]