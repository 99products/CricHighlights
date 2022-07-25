from deta import app
import telegram

import cric
import os
TELEGRAM_TOKEN = os.getenv('telegram_token').strip()
TELEGRAM_CHAT_ID = os.getenv('my_telegram_id').strip()

# define a function to run on a schedule
# the function must take an event as an argument
@app.lib.cron()
def cron_job(event):
    message=cric.check_highlights()
    if message:
        send_message(message)
    return "running on a schedule"

def send_message(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=message)
    return "message sent"
