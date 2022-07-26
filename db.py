import os
from deta import Deta

projectkey=os.getenv('project_key').strip()

deta = Deta(projectkey)
db = deta.Base("crichighlights")


def put_last_commentary(commentary):
    db.put(key='lastcommentary',data=commentary)

def get_last_commentary():
    return db.get(key='lastcommentary')