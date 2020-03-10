
from twilio.rest import Client

account_sid = 'AC0d6003d4a6ea0fb7e4c11bbf6efafea7' #This may differ from account to account
auth_token = 'Enter unique authentication token from your trillio account '
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='enter number obtained upon signing in Trillio',
    body='Hey ssup?',
    to='your own cellphone number'
)

print(message.sid)