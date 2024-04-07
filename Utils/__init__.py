import socket

# this function i use to get ip and forward to user discovery server
def getIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        # Get the local IP address
        local_ip = s.getsockname()[0]
        # Check if the IP address matches the desired format "10.x.x.x"
        print(local_ip)
        if local_ip.startswith('10.') or local_ip.startswith('127.0.0.1'):
            return local_ip
        else:
            raise ValueError("IP address does not match the desired format.")
    except Exception as e:
        print(f"An error occurred: {e}")

def getUserFromAddress(addr):
    import Discovery
    import requests
    params = {
        'HOST': Discovery.HOST,
        'PORT': Discovery.PORT,
        'USER': Discovery.USER
    }
    response = requests.put(Discovery.DISCOVERY_URL, json=params)
    discovery = response.json()
    for item in discovery:
        if item["HOST"] == addr[0]:
            return item["USER"]
    return None  # Return None if no matching object found
