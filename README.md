# recycle-reminder
A reminder for when you should take out recycling bin. This will run as a Microsoft Azure function and uses Twilio to send text messages

# Environment Variables
The following environment variables need to be set for this to work
- `ACCOUNT_SID` - The ID of your Twilio account
- `AUTH_TOKEN` - Your Twilio auth token
- `MESSAGING_SERVICE_SID` - SID of Twilio messaging service
- `PHONE_NUMBER` - The number to send the reminder to
- `TIMEZONE` - What TimeZone the check should be done in
