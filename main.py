from deta import app
import telegram
import db

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
    oldmessage=db.get_last_sent_message()
    if oldmessage['value']!=message:
        bot = telegram.Bot(token=TELEGRAM_TOKEN)
        if oldmessage and oldmessage['value'][:10]== message[:10]:
            print("message same as last message")
            messageid=db.get_last_message_id()
            if messageid:
                bot.editMessageText(chat_id=TELEGRAM_CHAT_ID, message_id=messageid, text=message)
        else:
            sentmessage = bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=message)
            db.put_last_message_id(sentmessage.message_id)
        db.put_last_sent_message(message)
        return "message sent"

cron_job(None)