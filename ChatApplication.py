import Messaging
import Discovery
import GUI
import time
import tkinter as tk

if __name__ == "__main__":
    Messaging.createListener() # For listening to messages
    time.sleep(1)
    Discovery.createListener() # For talking to central server
    while True:
        selection = int(input("Select a user: "))
        message = input("Enter a message: ")
        try:
            Messaging.sendMessage(Discovery.DISCOVERY[selection]['HOST'], int(Discovery.DISCOVERY[selection]['PORT']), message)
        except:
            print("There was an error attempting to send a message to that HOST and PORT.")
