import requests
from bs4 import BeautifulSoup

URL = "https://m.cricbuzz.com/"
filter_items = ['<b>FOUR</b>', '<b>SIX</b>', '<b>out</b>']


def check_highlights():
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    cricket_scores = soup.find_all(attrs={'class': 'cb-list-item'})

    if len(cricket_scores) > 1:
        commentaryurl = URL + cricket_scores[2].attrs['href']
        page = requests.get(commentaryurl)
        soup = BeautifulSoup(page.content, "html.parser")
        commentaries = soup.find_all(attrs={'class': 'commtext'})
        for commentary in commentaries:
            for filter in filter_items:
                if filter in str(commentary):
                    print(commentary)
                    break

# Run this in a cron job every 1 minute
# Store the last commentary text to check in next run
# For first run and also subsequent runs, check all latest commentaries until the last saved commentary
# Check for the pattern 'out', 'four', 'six', if in the latest commentaries you find any of these pattern,
# send notification to telegram channel

# print(job_elements)
