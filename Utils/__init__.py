import socket

# this function i use to get ip and forward to user discovery server
def getIP():
    try:
        # Get the local IP address
        local_ip = socket.gethostbyname(socket.gethostname())

        # Check if the IP address matches the desired format "10.x.x.x"
        if local_ip.startswith('10.'):
            return local_ip
        else:
            raise ValueError("IP address does not match the desired format.")
    except Exception as e:
        print(f"An error occurred: {e}")

def getUserFromAddress(addr):
    from Discovery import DISCOVERY
    for item in DISCOVERY:
        if item["HOST"] == addr[0]:
            return item["USER"]
    return None  # Return None if no matching object found
