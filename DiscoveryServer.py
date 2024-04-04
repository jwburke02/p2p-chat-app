from flask_restful import Resource, reqparse, Api
from flask import Flask
from threading import Thread
import time

active_users = [] # holds all active users
TTL = 30 # TTL constant

# define parser
parser = reqparse.RequestParser()
parser.add_argument('HOST', help="HOST cannot be blank.")
parser.add_argument('PORT', help="PORT cannot be blank.")
parser.add_argument('USER', help="PORT cannot be blank.")

def promptUsers(listof):
    for iter, user in enumerate(listof):
        print(f"{iter} - {user['USER']} ({user['HOST']})")

# Function to remove expired entries from the input list
def remove_expired_entries(data):
    current_time = time.time()
    data[:] = [entry for entry in data if current_time - entry.get('timestamp', 0) <= TTL]

class DiscoveryAPI(Resource):
    def put(self): # discovery server functionality
        try:
            # get 'HOST' and 'PORT'
            args = parser.parse_args()
            host = args['HOST']
            port = args['PORT']
            username = args['USER']
            # If already inside of the list, update the TTL and return the list
            for user in active_users:
                if user['HOST'] == host and user['PORT'] == port:
                    user['timestamp'] = time.time()
                    print("Updated user TTL - ", active_users)
                    return active_users
            # If not already inside of the list, create the entry
            new_user = {
                'HOST': host,
                'PORT': port,
                'USER': username,
                'timestamp': time.time()
            }
            active_users.append(new_user)
            print("Added new user - ", active_users)
            return active_users
        except:
            return "There was some issue with your request", 400
        
# configure endpoints
app = Flask(__name__)
api = Api(app)
api.add_resource(DiscoveryAPI, '/') # only API on server

# define and initialize listener
def deletorDaemon():
    while True:
        remove_expired_entries(active_users)
        print("Performed TTL Cleaning - ", active_users)
        time.sleep(TTL) 
listener = Thread(target=deletorDaemon)
listener.daemon = True
listener.start()

# driver code, host on 7777
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)

