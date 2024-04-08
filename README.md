# p2p-chat-app
This is a messaging application for two machines on the same local network. It works with user discovery through a centralized Flask server, and messaging functionality is directly p2p.
### Features
##### ChatApplication
- Read Messages: 
  - User is prompted to select a user they have previously messaged or to cancel
  - After user selection, all messages are displayed and all options are prompted
- Send Messages:
  - User is prompted to select a currently online user or to cancel
  - After user selection of an online user, they are allowed to enter a message and send it to this user. The user will have this message available next time they read messages, unless they have blocked the user attempting to send.
- Logout:
  - This quits the application.
- Manage Blocked Users:
  - User is prompted with a list of users, those that are blocked display a [BLOCKED] next to their name.
  - After user selection of a user from the list, it toggles and informs the user whether they have just blocked or unblocked the host.
##### DiscoveryServer
- PUT Endpoint
  - Parameters: String HOST, Int PORT, String USER
  - Returns: List of {HOST, PORT, USER}
  - This endpoint serves to keep a state of active users available at this server for any ChatApplication instances to reconcile the discovery list at any time.
- Note that this server's URL must be HARDCODED into each instance of ChatApplication.py, and only one machine should be running this DiscoveryServer.py
### Installation and Use
This application requires two machines on the same Wifi network to run. One machine must run both the DiscoveryServer and ChatApplication, with the DISCOVERY_URL in the Discovery module hardcoded. It should be localhost for the machine running DiscoveryServer. It should be some local address for the machine not running DiscoveryServer. Besides this URL configuration there is no additional setup, the system works entirely on the command line, and Discovery is handled automatically by the server. The messaging itself is still entirely peer-to-peer.
Note that this application requires MongoDB to be installed on the machine running it, as well as all dependencies in requirements.txt to be installed via pip: `pip install -r requirements.txt`.
