from urllib.request import urlopen
import re as r

# this function i use to get ip and forward to user discovery server
def getIP():
    d = str(urlopen('http://checkip.dyndns.com/').read())
    return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
