import sys
import json
import requests
from random import randint
import signal
import argparse


# Make sure to change these to your ZoomEye credentials
EMAIL = "CHANGETHIS@gmail.com"
PASSWD = "ChangeThis"

# API URL
URL = "https://api.zoomeye.org"

# General args variable
global args

# Safely stop the loops in case of CTRL+C
global interrputed
interrputed = False



# Random UA since its required (thanks for this @adcar)
def getRandomUserAgent():
    user_agents = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
                   "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
                   "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
                   "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1)",
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
                   "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
                   "Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.17",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0"]
    return user_agents[randint(0, len(user_agents) - 1)]


def getToken():
    print("[*] Logging in as "+args.email)
    headers = {
        'UserAgent': getRandomUserAgent()
    }

    USER_DATA = '{"username": ' + '"' + args.email + '"' + \
                ', "password":  ' + '"' + args.password + '"' + '}'

    AUTH_REQUEST = requests.post(URL + '/user/login', data=USER_DATA, headers=headers)

    try:
        # Wrong credentials
        if(AUTH_REQUEST.status_code == 403):
            raise KeyError
        print("access token: " + AUTH_REQUEST.text)
        ACCESS_TOKEN = AUTH_REQUEST.json()['access_token']
        print("[+] Successfuly logged in")
        return ACCESS_TOKEN
    except KeyError:
        # This isn't supressed in quiet mode because there won't bay any results
        print("[-] Invalid Credentials, please specify an email and password")
        sys.exit()
