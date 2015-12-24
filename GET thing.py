#!python 3.4

# Import stuff
import requests
import cloud_vars as cv #lol lazyness
from time import sleep

# Declare Vars

username = input("Enter your username: ")
password = input("Enter your password: ")
projectID = input("Enter the project ID: ")


#############################################################################
#                                                                           #
#                                   CHECKER                                 #
#                                                                           #
#############################################################################



s = cv.ScratchUserSession(username,password)
c= cv.CloudSession(projectID,s)

def sendGetReq(address):
    x = requests.get(address)
    while (x.status_code == 0):
        pass
    return x
def checkVal(var):
    return s.cloud.get_var(var, projectID)

def myEncode(text):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+[]\{}|;':\",./<>?`~"
    total = ""
    for l in text:
        toAdd = str(chars.find(l)+1)
        if len(toAdd)==1:
            toAdd="0" + toAdd
        total+=toAdd
    total = int(total)
    return total

def myDecode(string):
    total = ""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+[]\{}|;':\",./<>?`~"
    for i in range(0,len(string),2):

        total+=chars[(int(string[i]+string[i+1])-1)]
    return total


print("starting...")
while True:
    sleep(1)

    if (int(checkVal("Waiting")) == 1):
            print("It's one...")
            to_encode = sendGetReq(myDecode(checkVal("Send"))).text
            to_send = myEncode(to_encode)
            c.set_var("Recieve",to_send)
            c.set_var("Waiting",0)
            print("sent...\n")









