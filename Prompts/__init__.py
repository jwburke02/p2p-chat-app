def promptUser():
    print("--------------------------------------")
    print("AVAILABLE OPTIONS:")
    print("--------------------------------------")
    print("1 - Read Messages from a user")
    print("2 - Send Messages to a user")
    print("3 - Logout")
    print("4 - Manage blocked users")
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

def promptBlock(discovery):
    print("--------------------------------------")
    print("POSSIBLE USERS TO BLOCK:")
    print("--------------------------------------")
    for iter, user in enumerate(discovery):
        print(f"{iter + 1} - {user['USER']} ({user['HOST']})")
    print("--------------------------------------")
    result = int(input("Make a selection to toggle Block/Unblock: "))
    print("\n")
    return result - 1