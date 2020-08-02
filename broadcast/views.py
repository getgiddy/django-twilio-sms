from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client
from twilio.rest import TwilioException


def broadcast_sms(request):
    message_to_broadcast = "Have you played the incredible TwilioQuest yet? Grab it here: https://www.twilio.com/quest"
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    SMS_BROADCAST_TO_NUMBERS = [
        "+2349014610125",  # use the format +19735551234
        "+2349055647406",
        "+2349055648406",
    ]
    for recipient in SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            try:
                client.messages.create(
                    to=recipient,
                    from_=settings.TWILIO_NUMBER,
                    body=message_to_broadcast
                )
            except TwilioException:
                pass
    return HttpResponse("messages sent!", 200)
