# python prog to check email account across service
# install holehe module

import subprocess

def check_email(email):
    result = subprocess.run(['holehe', email], capture_output= True, text=True)
    return result.stdout

email = input('Enter Your Email: ')
response = check_email(email)
print(response)

