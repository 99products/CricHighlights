# CricHighlights
Automated bot which sends cricket commentaries (only the highlights) to telegram channel

This project is created for learning,

1. Web Scraping in python
2. Server hosting with deta.sh
3. Telegram Bot Integration
4. CICD with github actions


### Web Scraping in python

The live commentary is fetched by scrapping m.cricbuzz.com, using python library ['BeautifulSoup'](https://beautiful-soup-4.readthedocs.io/en/latest/ "'BeautifulSoup'")

The sample code to parse the commentaries,

> soup = BeautifulSoup(page.content, "html.parser")

> commentaries = soup.find_all(attrs={'class': 'commtext'})

### Server hosting with deta.sh

We need a cloud server to host our code and also to run it periodically. 
I have worked in all major to small cloud providers GCP, AWS, Azure, firebase and heroku.

But IMO [deta.sh](https://deta.sh "deta.sh") is my favorite for its simplicity. 

1.  Follow the process here -> https://docs.deta.sh/docs/micros/getting_started 
	- Signup 
	- Install 
	- Login to deta CLI
	- Create new Deta micro
2. For our project, we need a cron job to be setup to periodically check the commentary page
	- Setup a cron following the sample here -> https://docs.deta.sh/docs/micros/cron
	- Set the deta cron for "1 minute"
	- our sample code:
		```
		@app.lib.cron()
		def cron_job(event):
			message=cric.check_highlights()
			if message:
				send_message(message)
			return "running on a schedule"
		```
3. Once deployed, enable the log, and confirm if the schedule is working properly in the 'visor' tab of your micro in web.deta.sh dashboard

4. We also use Deta base for our duplicate check (check db.py),  Checkout the doc here for the usage --> https://docs.deta.sh/docs/base/sdk

5. The project key to use deta can be retrieved from,
     https://web.deta.sh/home/%username%/default/settings/

6. All our secrets ( deta project key, telegram token etc.. ) cannot be exposed in our code, so we need to refer from environment variables.
To set the environment variables in deta, add all your keys in a file called .env,  as key-value pairs, and update it to deta using the following command.

	> deta update -e .env




### Telegram Bot Integration

1. Create a telegram channel

2. Create a telegram bot using botfather, checkout the doc here --> https://core.telegram.org/bots 

3. Set the channel name and bot token as environment variables and update to our deta micro. ( refer main.py for the keys used )

4. Use the library, *python-telegram-bot* to send message to your telegram channel, 
   sample code here,
   
	> bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=message) 




### CICD with Github actions

Github actions helps to deploy code automatically to deta.sh on commit/push new changes.

1. Go to 'Actions' tab in your github repository

2. Create a new workflow and in actions search for 'deta.sh' 

3. Check the sample workflow here --> https://github.com/BogDAAAMN/deta-deploy-action

4. Get the deta project key from here -> https://web.deta.sh/home/%username%/

5. Set the projectkey as 'DETA_TOKEN' secret in your repository -> settings/secrets/actions , which will be referred in your action

6. Once set, for every push to the repository the changes will be automatically deployed to deta
