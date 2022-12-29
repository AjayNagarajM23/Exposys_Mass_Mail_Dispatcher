import time

import pandas as pd
import requests
import re

data = pd.read_csv('Mails.csv')

mails = data['mail']

for ele in mails:
    ele = ele + ""
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat, ele):
        response = requests.get(
            "https://isitarealemail.com/api/email/validate",
            params={'email': ele})
        print(ele+" : "+str(response))
        print(response.json())

    time.sleep(5)
