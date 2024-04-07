import Messaging
import Discovery
import time
import Database
import requests
from Prompts import *

if __name__ == "__main__":
    # Progress Loop
    logged_in = False
    while True:
        if not logged_in:
            user = input("Enter your Username: ")
            Messaging.createListener()
            Discovery.updateUser(user)
            time.sleep(1)
            Discovery.createListener()
            logged_in = True
        else:
            selection = promptUser()
            if selection == 1:
                connected_users = Database.retrieveConnectionsList()
                # Prompt for select from a users list
                user_selection = promptRead(connected_users)
                if user_selection == -1:
                        print('\n')
                else:
                    # Message history for that user's IP will be taken from DB and printed
                    if Database.hostExistsInCollection(connected_users[user_selection]['HOST'], connected_users[user_selection]['USER']):
                        messages = Database.getMessagesFromHostDoc(connected_users[user_selection]['HOST'], connected_users[user_selection]['USER'])
                        printMessages(messages, connected_users[user_selection]['USER'])
                    else:
                        print("No messages found.")
            if selection == 2:
                try:
                    # quickly get updated discovery list 
                    params = {
                        'HOST': Discovery.HOST,
                        'PORT': Discovery.PORT,
                        'USER': Discovery.USER
                    }
                    response = requests.put(Discovery.DISCOVERY_URL, json=params)
                    discovery = response.json()
                    mod = True
                    while mod:
                        mod = False
                        for item in discovery:
                            if item['HOST'] == Discovery.HOST or Database.isHostBlocked(item['HOST']):
                                mod = True
                                discovery.remove(item)
                    [user_selection, message] = promptWrite(discovery)
                    if user_selection == -1:
                        print('\n')
                    else:
                        Messaging.sendMessage(discovery[user_selection]['HOST'], int(discovery[user_selection]['PORT']), message, discovery[user_selection]['USER'])
                except:
                    print(f"There was an error attempting to send a message to that HOST and PORT: {Discovery.DISCOVERY[user_selection]['HOST']},{Discovery.DISCOVERY[user_selection]['PORT']}")
            if selection == 3:
                # End program, this will cut
                print('\n')
                print('LOGGING OUT...')
                print('\n')
                quit()
            if selection == 4:
                try:
                    # quickly get updated discovery list 
                    params = {
                        'HOST': Discovery.HOST,
                        'PORT': Discovery.PORT,
                        'USER': Discovery.USER
                    }
                    response = requests.put(Discovery.DISCOVERY_URL, json=params)
                    discovery = response.json()
                    mod = True
                    while mod:
                        mod = False
                        for item in discovery:
                            if item['HOST'] == Discovery.HOST:
                                mod = True
                                discovery.remove(item)
                    user_selection = promptBlock(discovery)
                    if user_selection == -1:
                        print('\n')
                    else:
                        Database.toggleBlock(discovery[user_selection]['HOST'])
                        if Database.isHostBlocked(discovery[user_selection]['HOST']):
                            print("Host blocked...")
                        else:
                            print("Host unblocked...")
                        
                except:
                    print(f"There was an error attempting to block that HOST and PORT: {Discovery.DISCOVERY[user_selection]['HOST']},{Discovery.DISCOVERY[user_selection]['PORT']}")
