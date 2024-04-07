import Messaging
import Discovery
import time
import Database
import requests

def promptUser():
    print("--------------------------------------")
    print("AVAILABLE OPTIONS:")
    print("--------------------------------------")
    print("1 - Read Messages from a user")
    print("2 - Send Messages to a user")
    print("3 - Logout")
    print("4 - Mute or Block a user")
    print("--------------------------------------")
    result = int(input("Make a selection: "))
    print("\n")
    return result

def promptRead(connected_users):
    print("--------------------------------------")
    print("MESSAGE HISTORY:")
    print("--------------------------------------")
    for iter, user in enumerate(connected_users):
        print(f"{iter + 1} - {user['USER']} ({user['HOST']})")
    print("--------------------------------------")
    result = int(input("Make a selection: "))
    print("\n")
    return result - 1

def printMessages(messages, user):
    print("--------------------------------------")
    print(f"MESSAGE HISTORY WITH {user}:")
    print("--------------------------------------")
    for iter, message in enumerate(messages):
        text = message['message']
        was_sent = message['sent']
        if was_sent:
            print(f"{iter + 1} - From you: {text}")
        else:
            print(f"{iter + 1} - From {user}: {text}")
    print("--------------------------------------")
    print("\n")
    return

def promptWrite(discovery):
    print("--------------------------------------")
    print("ONLINE RECIPIENTS:")
    print("--------------------------------------")
    for iter, user in enumerate(discovery):
        print(f"{iter + 1} - {user['USER']} ({user['HOST']})")
    print("--------------------------------------")
    result = int(input("Make a selection: "))
    message = input("Write a message: ")
    print("\n")
    return [result - 1, message]

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
                    [user_selection, message] = promptWrite(discovery)
                    Messaging.sendMessage(discovery[user_selection]['HOST'], int(discovery[user_selection]['PORT']), message, discovery[user_selection]['USER'])
                except:
                    print(f"There was an error attempting to send a message to that HOST and PORT: {Discovery.DISCOVERY[user_selection]['HOST']},{Discovery.DISCOVERY[user_selection]['HOST']}")
            if selection == 3:
                # End program, this will cut
                quit()
            if selection == 4:
                # Prompt user for select from users list
                Discovery.promptUsers()
                user_selection = input("Select a user: ")
                # Then block or mute
