import Messaging
import Discovery
import time
import Database

def promptUser():
    print("Options: ")
    print("1 - Read Messages from a user")
    print("2 - Send Messages to a user")
    print("3 - Logout")
    print("4 - Mute or Block a user")
    return int(input("Make a selection: "))


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
                # Prompt for select from a users list
                Discovery.promptUsers()
                user_selection = int(input("Select a user: "))
                # Message history for that user's IP will be taken from DB and printed
                if Database.hostExistsInCollection(Discovery.DISCOVERY[user_selection]['HOST'], Discovery.DISCOVERY[user_selection]['USER']):
                    messages = Database.getMessagesFromHostDoc(Discovery.DISCOVERY[user_selection]['HOST'], Discovery.DISCOVERY[user_selection]['USER'])
                    for message in messages:
                        print(message['message'])
                else:
                    print("No messages found.")
            if selection == 2:
                # Prompt for select from a users list
                Discovery.promptUsers()
                user_selection = int(input("Select a user: "))
                # User selects individual and enters message
                message = input("Enter message: ")
                try:
                    Messaging.sendMessage(Discovery.DISCOVERY[user_selection]['HOST'], int(Discovery.DISCOVERY[user_selection]['PORT']), message, Discovery.DISCOVERY[user_selection]['USER'])
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
