import requests
from threading import Thread
import time
import Utils

# server URL (for discovery)
DISCOVERY_URL = "http://localhost:7777/"

# gets updated prior to discoveryListener execution
HOST = Utils.getIP()
PORT = -1
USER = ""
DISCOVERY = []

def promptUsers():
    for iter, user in enumerate(DISCOVERY):
        print(f"{iter} - {user['USER']} ({user['HOST']})")

def updatePort(port):
    global PORT
    PORT = port

def updateUser(user):
    global USER 
    USER = user

'''
This call is made every ~20 seconds to the server to update discoveries list
'''
def discoveryListener():
    while True:
        params = {
            'HOST': HOST,
            'PORT': PORT,
            'USER': USER
        }
        response = requests.put(DISCOVERY_URL, json=params)
        global DISCOVERY
        DISCOVERY = response.json()
        time.sleep(20)

def createListener():
    listener = Thread(target=discoveryListener)
    listener.daemon = True
    listener.start()

'''
Uses the previously created discovery_dict in order to 
display to the user integer options for selecting who to message
'''
def displayDiscoveries(discovery_dict):
    print("Available for messaging: ")
    for key in discovery_dict:
        print(f"    {key}: {discovery_dict[key]['USER']}")