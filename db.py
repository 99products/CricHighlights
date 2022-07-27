import os
from deta import Deta

projectkey=os.getenv('project_key').strip()

deta = Deta(projectkey)
db = deta.Base("crichighlights")


def put_last_sent_message(message):
    db.put(key='lastsentmessage',data=message)

def get_last_sent_message():
    lastsentmessage= db.get(key='lastsentmessage')
    if lastsentmessage:
        return lastsentmessage['value']

def put_last_message_id(message):
    db.put(key='lastmessageid',data=message)

def get_last_message_id():
    lastmessageid= db.get(key='lastmessageid')
    if lastmessageid:
        return lastmessageid['value']
