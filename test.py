import requests


def verify_mail(email_address):
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params={'email': email_address})

    status = response.json()['status']
    if status == "valid":
        print("email is valid"+email_address)
    elif status == "invalid":
        print("email is invalid"+email_address)
    else:
        print("email was unknown"+email_address)
