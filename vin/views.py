import string

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import pandas as pd
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail
import requests
import time
import re


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, username + " Successfully Logged In")
            return redirect('index')
        else:
            messages.error(request, "Bad credentials ( Wrong Username Or Password )")
            return redirect('signin')
    return render(request, 'login.html')


def verifymail(request):
    if request.method == 'POST':
        file = request.FILES["myFile"]
        df = pd.read_csv(file)
        arr = df["mail"]

        for ele in arr:
            ele = ele + ""
            email_address = ele

            pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.match(pat, email_address):
                response = requests.get(
                    "https://isitarealemail.com/api/email/validate",
                    params={'email': email_address})

                status = response.json()['status']

                if status == "valid":
                    continue
                elif status == "invalid":
                    messages.warning(request, ele)
                else:
                    messages.warning(request, ele)
            else:
                messages.warning(request, ele)

            time.sleep(2)
        return render(request, 'infomail.html')
    return render(request, 'verifymail.html')


def signout(request):
    logout(request)
    return redirect('signin')


def infomail(request):
    return render(request, 'infomail.html')


def sendmail(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        content = request.POST['content']
        # deltime = request.POST['delay']
        file = request.FILES["myFile"]
        df = pd.read_csv(file)
        arr = df["mail"]
        # time.sleep(int(deltime)*60)

        for ele in arr:
            ele = ele + ""
            pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.match(pat, ele):
                response = requests.get(
                    "https://isitarealemail.com/api/email/validate",
                    params={'email': ele})
                status = response.json()['status']
                if status == "valid":
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [ele]
                    send_mail(subject, content, email_from, recipient_list)
                    messages.info(request, ele)
                elif status == "invalid":
                    messages.warning(request, ele)
                else:
                    messages.warning(request, ele)
            else:
                messages.warning(request, ele)

            time.sleep(2)
        return render(request, 'confirmation.html')
    return render(request, 'sendmail.html')


def confirmation(request):
    return render(request, 'confirmation.html')
