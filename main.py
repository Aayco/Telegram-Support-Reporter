ple Say You Can't Make A Telegram Reporter With Only Requests So I Will Show Them How
#Check If Requests Module Installed
try:
    from requests import post as p
#If Not Installed
except ImportError:
    print('Requests Module Not Installed Install It By This Command `pip install requests`')
#Telegram Support Website
url = "https://telegram.org/support"
#The Headers That We Will Use
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://telegram.org",
    "priority": "u=0, i",
    "referer": "https://telegram.org/support",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"
}

#The Cute User Inputs
#Input Your Account Number
phone_number = input('Enter Your Phone Number: ')
#Input Issue Message
issue_message = input('Enter Your Issue: ')
#Input Your Full Legal Name
full_name = input('Enter Your Full Legal Name: ')
#Input Email For Contact
email = input('Enter Your Email: ')
#Input The Page Language
language = input('Enter The Page Language (ex: en for engilsh or ar for arabic): ')

#The Data That Contain Your Info
data = {
    #Your Issue Message
    "message": issue_message,
    #Your Full Legal Name
    "legal_name": full_name,
    #Your Email For Contact
    "email": email,
    #Your Account Number
    "phone": phone_number,
    #The Page Language
    "setln": language
}
#Send The Info To The Telegram Support Web
try:
    response = p(url, headers=headers, data=data)
    #Print Response Status Code (200 = Success)
    print("Status Code:", response.status_code)
    #Check If Issue Sent To Telegram Successfully
    if response.status_code == 200 and '<div class="alert alert-success">' in (response.text):
        #Print Success Message
        print(f'Issue Message: {issue_message}\nFull Legal Name {full_name}\nFor Number: {phone_number}\nHas Been Succesfully Sent To {url}\nCheck Your Email {email} For Any Reply From Telegram Support')
    else:
        #Prrint Failure Message
        print('There Is Something Wrong Happend')
#Error Handling
except Exception as e:
    print(f'Error: {e}')    
