import pymongo
import datetime

DB_CLIENT = pymongo.MongoClient('mongodb://localhost:27017')

DB = DB_CLIENT['p2p-chat']

MESSAGES_COLLECTION = DB['message']
# OBJECT 
# MESSAGECONTAINER
# _ID ObjectID("")
# HOST ""
# MESSAGES []

# MESSAGE_OBJECT
# timestamp
# message
# sent - bool (false if a received message)

#############
# OBJECT CREATION
#############
def createHostDoc(host, user, message, sent):
    current_time_seconds = datetime.datetime.now().timestamp()
    message_obj = {
        "message": message,
        "sent": sent,
        "timestamp": current_time_seconds
    }
    new_doc = {
        "HOST": host,
        "USER": user,
        "MESSAGES": [message_obj],
        "IS_MUTED": False,
        "IS_BLOCKED": False
    }
    # insert into collection
    result = MESSAGES_COLLECTION.insert_one(new_doc)
    if result.inserted_id:
        return 
    else:
        raise Exception("Unable to create message object.")
    
#############
# MESSAGE SENDING
#############
def addMessageToHostDoc(host, user, message, sent):
    current_time_seconds = datetime.datetime.now().timestamp()
    message_obj = {
        "message": message,
        "sent": sent,
        "timestamp": current_time_seconds
    }
    result = MESSAGES_COLLECTION.update_one({"HOST": host, "USER": user}, {"$push": {"MESSAGES": message_obj}})

#############
# MESSAGE RETRIEVAL
#############
def getMessagesFromHostDoc(host, user):
    current_object = MESSAGES_COLLECTION.find_one({"HOST": host, "USER": user})
    messages = current_object['MESSAGES']
    return messages

#############
# CHECK IF HOST EXISTS 
#############
def hostExistsInCollection(host, user):
    current_object = MESSAGES_COLLECTION.find_one({"HOST": host, "USER": user})
    if current_object:
        return True
    else:
        return False
    
#############
# CONNECTIONS RETRIEVAL
#############
def retrieveConnectionsList():
    results = MESSAGES_COLLECTION.find({})
    list = []
    for doc in results:
        if not doc['IS_BLOCKED']:
            list.append(doc)
    if (results):
        return list
    else:
        return None
    
#############
# TOGGLE USER BLOCK
#############
def toggleBlock(host):
    # this will toggle block for every host, so a host can either be fully blocked or not fully blocked
    orig = MESSAGES_COLLECTION.find_one({"HOST": host})
    to_set = not orig['IS_BLOCKED']
    result = MESSAGES_COLLECTION.update_many(
        {"HOST": host},
        {"$set": {"IS_BLOCKED": to_set}}
    )
    if (result):
        return True
    else:
        return False
#############
# CHECK IF BLOCKED
#############
def isHostBlocked(host):
    result = MESSAGES_COLLECTION.find_one({"HOST": host})['IS_BLOCKED']
    return result

#############
# TOGGLE USER MUTE
#############
def toggleMute(host):
    # this will toggle block for every host, so a host can either be fully blocked or not fully blocked
    orig = MESSAGES_COLLECTION.find_one({"HOST": host})
    to_set = not orig['IS_MUTED']
    result = MESSAGES_COLLECTION.update_many(
        {"HOST": host},
        {"$set": {"IS_MUTED": to_set}}
    )
    if (result):
        return True
    else:
        return False
#############
# CHECK IF MUTED
#############
def isHostMuted(host):
    result = MESSAGES_COLLECTION.find_one({"HOST": host})['IS_MUTED']
    return result