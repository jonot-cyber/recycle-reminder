import datetime
import logging

import azure.functions as func

import pytz
import os

from twilio.rest import Client

def send_message(recycle: bool) -> None:
    twilio_client = Client(os.environ["ACCOUNT_SID"], os.environ["AUTH_TOKEN"])
    messaging_service_sid = os.environ["MESSAGING_SERVICE_SID"]
    send_to = os.environ["PHONE_NUMBER"]

    message: str
    if recycle:
        message = "This week is recycling week"
    else:
        message = "This week is not recycling week"
    twilio_client.messages.create(to=send_to, messaging_service_sid=messaging_service_sid, body=message)

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    timezone = pytz.timezone(os.environ["TIMEZONE"])

    today = datetime.datetime.now(tz=timezone)

    # if its not tuesday, don't bother
    if today.weekday() != 1:
        return

    epoch = datetime.datetime(2022, 12, 13, tzinfo=timezone)

    elapsed_time = today - epoch
    days_since_epoch = elapsed_time.days
    weeks_since_epoch = days_since_epoch // 7

    send_message(weeks_since_epoch % 2 == 0)
