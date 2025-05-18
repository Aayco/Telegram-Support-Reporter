#Check If Requests Module Installed
import os
try:
    from requests import post as p
    from faker import Faker
    import random
#If Not Installed
except ModuleNotFoundError as e:
    module_name = str(e).split("'")[1]
    print(f'Module {module_name} Not Found Installing It Now...')
    os.system(f'pip install {module_name}')
#Telegram Support Website
url = "https://telegram.org/support"
#The Headers That We Will Use
headers = {
    'authority': 'telegram.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://telegram.org',
    'referer': 'https://telegram.org/support',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
}

#The Cute User Inputs
#Input Your Account Number
phone_number = '+20××××××××××'
#Input Your Account Username
username = '@iAiyko'
#Input Issue Message
issue_message = f'''
Hello Telegram Support Team,
My name is [Amiru My Username Is {username}], and my account/phone number has been banned without any prior warning. I am not aware of any specific reason for this ban.
I would like to clarify that I have not engaged in any activity that violates Telegram's terms of service or causes inconvenience to other users.
I kindly request you to review my case and lift the ban on my account as soon as possible, as I rely on Telegram for both personal and professional communication.
Thank you for your support.
Best regards,
[Phone Number Linked to the Account: {phone_number}]
'''
# For Full Legal Name Field
name = (Faker()).name()
# To Generate Random Number For Email
num = str(random.randint(1000, 9999))
# Contact Email
email = (name+num+'@gmail.com').replace(' ', '')
#Input The Page Response Language
language = 'en'

#The Data That Contain Your Info
data = {
    #Your Issue Message
    "message": issue_message.replace('\n', ' '),
    #Your Full Legal Name
    "legal_name": name,
    #Your Email For Contact
    "email": email,
    #Your Account Number
    "phone": phone_number,
    #The Page Language
    "setln": language
}
#Send The Info To The Telegram Support Web
while True:
 try:
    response = p(url, headers=headers, data=data)
    #Print Response Status Code (200 = Success)
    print("Status Code:", response.status_code)
    #Check If Issue Sent To Telegram Successfully
    if response.status_code == 200 and '<div class="alert alert-success">' in (response.text):
        #Print Success Message
        print(f'Issue Message: {issue_message}\nFull Legal Name {name}\nFor Number: {phone_number}\nHas Been Succesfully Sent To {url}\nCheck Your Email {email} For Any Reply From Telegram Support')
    else:
        #Prrint Failure Message
        print('There Is Something Wrong Happend')
 #Error Handling
 except Exception as e:
    print(f'Error: {e}')    
