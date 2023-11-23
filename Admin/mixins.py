from django.conf import settings
from twilio.rest import Client 

import os


import random

class MessaHandler:

    phone_number=None 
    otp =None

    def __init__(self,phone_number,otp)->None:
        self.phone_number=phone_number
        self.otp=otp
        


    def send_otp_on_phone(self):
        account_sid = "AC8e48715c6a096f38bc6768602b82270a"
        auth_token = "9d0a8b627186031f8ce12aee5d2605de"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                      body=f'Therapy Excellence--your otp is {self.otp}',
                                      from_='+16206282990',
                                      to=self.phone_number
                                  )
        print('message sent successfully')

   


