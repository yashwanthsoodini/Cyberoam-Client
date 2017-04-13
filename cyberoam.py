#!/usr/bin/python
import requests
import sys
import threading

username = "USERNAME_GOES_HERE"
password = "PLAINTEXT_PASSWORD_GOES_HERE"
gateway = "CYBEROAM_GATEWAY_GOES_HERE"
global url, logged_in
logged_in = False
port = "GATEWAY_PORT_GOES_HERE"
url = "http://{}:{}/httpclient.html".format(gateway, port)


def login():
    global url, username, password, logged_in
    try:
        data_login = {'mode': 191, 'username': username, 'password': password, 'btnSubmit': 'Login'}
        r = s.post(url, data=data_login)
    except Exception:
        print "Error during login. Make sure your username and password is correct."
        logged_in = False
    else:
        if not logged_in:
            print "Logged In."
        logged_in = True
        # print "Thread count: {}".format(threading.activeCount())
        # login every 600 seconds to prevent timeout
        t = threading.Timer(600.0, login)
        t.setDaemon(True)
        t.start()


def logout():
    global url, username, password
    try:
        data = {'mode': 193, 'username': username, 'password': password, 'btnSubmit': 'Logout'}
        r = s.post(url, data=data)
    except Exception:
        print "Error during logout. Logout via webclient."
    else:
        print "Logged Out."
        sys.exit()


with requests.Session() as s:
        login()
        if logged_in:
            inp = raw_input("Press 'Enter' to logout.")
            logout()
        else:
            print "Error during login. Make sure your username and password is correct."
            sys.exit()

# v.2.0 - current version uses 2 threads, but only checks for Response Code 200 during login
# Sridhama Prakhya
# sridhama.com
