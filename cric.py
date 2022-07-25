import requests
from bs4 import BeautifulSoup
from deta import Deta

import os
projectkey=os.getenv('project_key').strip()

URL = "https://m.cricbuzz.com/"
filter_items = ['<b>FOUR</b>', '<b>SIX</b>', '<b>out</b>']
deta = Deta(projectkey)
db = deta.Base("crichighlights")


# Store the last commentary text to check in next run
# For first run and also subsequent runs, check all latest commentaries until the last saved commentary
# Check for the pattern 'out', 'four', 'six', if in the latest commentaries you find any of these pattern,

#TODO The same commentary will be updated, e.g. if someone is out, the same commentary line will be updated with more info,resulting in duplicate messages
#TODO find ways to send commentary only for india matches
#TODO look for patterns and try to improve it further
#TODO add formatting to the messages

def check_highlights():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    cricket_scores = soup.find_all(attrs={'class': 'cb-list-item'})
    if len(cricket_scores) > 1:
        commentaryurl = URL + cricket_scores[2].attrs['href']
        page = requests.get(commentaryurl)
        soup = BeautifulSoup(page.content, "html.parser")
        commentaries = soup.find_all(attrs={'class': 'commtext'})
        count=0
        last_commentary = get_last_commentary()
        for commentary in commentaries:
            if(count==0):
                put_last_commentary(commentary.text)
            count=count+1
            if last_commentary['value'] == commentary.text:
                break
            for filter in filter_items:
                if filter in str(commentary):
                    return commentary.text

def put_last_commentary(commentary):
    db.put(key='lastcommentary',data=commentary)

def get_last_commentary():
    return db.get(key='lastcommentary')

check_highlights()





# print(job_elements)
