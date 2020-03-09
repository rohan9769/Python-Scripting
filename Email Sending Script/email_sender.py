import smtplib #^SMTP allows to create an SMTP server between browser and server
from email.message import EmailMessage
from string import Template #used for mapping
from pathlib import Path #allows to access external files,like here index.html

#Sending email basics

# email = EmailMessage()
# email['from'] = 'Leo d'     #denotes the sender
# email['to'] = 'leodsouza2071@gmail.com' #denotes recipient
# email['subject'] = 'You won 100$'
#
# email.set_content('I am master at Python Scripting')
#
#
# with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
#     smtp.ehlo() #part of SMTP protocol
#     smtp.starttls() #tls is an encryption,means connect securely
#     smtp.login('leodsouza2071@gmail.com','Rohan257') #To login to account
#     smtp.send_message(email)
#     print('all good!')


#Sending custom emails

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Leo d'     #denotes the sender
email['to'] = 'leodsouza2071@gmail.com' #denotes recipient
email['subject'] = 'You won 100$'

email.set_content(html.substitute({'name':'Roger'}),'html')


with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo() #part of SMTP protocol
    smtp.starttls() #tls is an encryption,means connect securely
    smtp.login(' ',' ') #To login to account ,smtp.login('emailaddress','password')
    smtp.send_message(email)
    print('all good!')


