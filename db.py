import os
from deta import Deta

# projectkey=os.getenv('project_key').strip()
projectkey='a0mmxdo6_4bKC7Q8nek8yT3Q4CXMWQgKKkwV1aYjB'

deta = Deta(projectkey)
db = deta.Base("crichighlights")


def put_last_commentary(commentary):
    db.put(key='lastcommentary',data=commentary)

def get_last_commentary():
    return db.get(key='lastcommentary')

def put_last_sent_message(message):
    db.put(key='lastsentmessage',data=message)

def get_last_sent_message():
    return db.get(key='lastsentmessage')

def put_last_message_id(message):
    db.put(key='lastmessageid',data=message)

def get_last_message_id():
    return db.get(key='lastmessageid')
