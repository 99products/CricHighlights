# CricHighlights
Automated bot which sends cricket commentaries (only the highlights) to telegram channel

This project is created for learning,

1. Web Scraping in python
2. Server hosting with deta.sh
3. Telegram Bot Integration
4. CICD with github actions


#### Web Scraping in python

The live commentary is fetched by scrapping m.cricbuzz.com, using python library ['BeautifulSoup'](https://beautiful-soup-4.readthedocs.io/en/latest/ "'BeautifulSoup'")

Scraping is simple and all we need to do is look for the right pattern and the tag or class or id to fetch the right data.  The sample code to parse the commentaries,

> soup = BeautifulSoup(page.content, "html.parser")
commentaries = soup.find_all(attrs={'class': 'commtext'})

#### Server hosting with deta.sh

Now we need a server to host our code and also to run it periodically. 
IMO, i have worked in all major to small cloud providers GCP, AWS, Azure, firebase and heroku.  
But [deta.sh](https://deta.sh "deta.sh") is my favorite for its simplicity. 



