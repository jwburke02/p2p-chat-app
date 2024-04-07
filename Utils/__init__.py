# this function i use to get ip and forward to user discovery server
def getIP():
    try:
        from requests import get
        ip = get('https://api.ipify.org').content.decode('utf8')
        if (ip):
            return ip
        else:
            raise ValueError("Could not find IP address.")
    except Exception as e:
        print(f"An error occurred: {e}")

def getUserFromAddress(addr):
    from Discovery import DISCOVERY
    for item in DISCOVERY:
        if item["HOST"] == addr[0]:
            return item["USER"]
    return None  # Return None if no matching object found
