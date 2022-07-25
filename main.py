from deta import app

import cric

# define a function to run on a schedule
# the function must take an event as an argument
@app.lib.cron()
def cron_job(event):
    cric.check_highlights()
    return "running on a schedule"