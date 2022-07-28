import re

import requests
from bs4 import BeautifulSoup

URL = "https://m.cricbuzz.com/"
filter_items = ['<b>FOUR</b>', '<b>SIX</b>', '<b>out</b>']

#TODO #3 find ways to send commentary only for india matches
#TODO #4 add formatting to the messages

def check_highlights():
    '''
Parse home page, get the first match listed
List all the commentaries
Check for the pattern, and return first matching commentary
'''
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    cricket_scores = soup.find_all(attrs={'class': 'cb-list-item'})
    if len(cricket_scores) > 1:
        commentaryurl = URL + cricket_scores[2].attrs['href']
        page = requests.get(commentaryurl)
        soup = BeautifulSoup(page.content, "html.parser")
        scores=soup.find(attrs={'class':re.compile('ui-bat-team-scores')})
        batteamscore=''
        bowlteamscore=''
        if scores:
            batteamscore=scores.text
        scores=soup.find(attrs={'class':re.compile("ui-bowl-team-scores")})
        if scores:
            bowlteamscore=scores.text
        status = soup.find(attrs={'class': 'cbz-ui-status'})
        #if status found, then match is over or stumps
        if status:
            print(status.text)
            return status.text+'\n'+batteamscore+'\n'+bowlteamscore
        
        commentaries = soup.find_all(attrs={'class': 'commtext'})
        for commentary in commentaries:
            for filter_item in filter_items:
                if filter_item in str(commentary):
                    return commentary.text+"\n\n"+batteamscore+"\n"+bowlteamscore
