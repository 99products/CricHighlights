import requests
import db
from bs4 import BeautifulSoup
from deta import Deta



URL = "https://m.cricbuzz.com/"
filter_items = ['<b>FOUR</b>', '<b>SIX</b>', '<b>out</b>']

#TODO The same commentary will be updated, e.g. if someone is out, the same commentary line will be updated with more info,resulting in duplicate messages
#TODO #3 find ways to send commentary only for india matches
#TODO look for patterns and try to improve it further
#TODO #4 add formatting to the messages

def check_highlights():
    '''
Store the last commentary text to check in next run
For each run, check all latest commentaries until the last saved commentary
Check for the pattern, and filter commentaries
'''
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    cricket_scores = soup.find_all(attrs={'class': 'cb-list-item'})
    if len(cricket_scores) > 1:
        commentaryurl = URL + cricket_scores[2].attrs['href']
        page = requests.get(commentaryurl)
        soup = BeautifulSoup(page.content, "html.parser")
        commentaries = soup.find_all(attrs={'class': 'commtext'})
        count=0
        last_commentary = db.get_last_commentary()
        for commentary in commentaries:
            if count==0:
                db.put_last_commentary(commentary.text)
            count=count+1
            if last_commentary['value'] == commentary.text:
                break
            for filter_item in filter_items:
                if filter_item in str(commentary):
                    return commentary.text

print(check_highlights())

# print(job_elements)
