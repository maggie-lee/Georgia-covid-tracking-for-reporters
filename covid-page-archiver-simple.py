#!/usr/bin/python3.6

import requests

# This is the most simple way to submit a page to the internet archive. It doesn't have a timer, it doesn't check when
# the page was last submitted to internet archive.

# To make this run, you'd save this as a .py file set it up somewhere as a scheduled task. You might need to change that very top 
# line too, depending on your Python setup. One way that usually works on macs anyway is: #!/usr/bin/python3

# There are many ways to schedule running a .py file. These are only two:
#
# 1. It could be as a cron task (a task timing system built into your compuer) on your own computer, like run at 5 am and 5 pm:  
# 0 5,17 * * * python /path_to/the_script.py
# But your computer has to be on for a cron task. 
#
# 2. I myself run this code twice a day as a scheduled task on PythonAnywhere, a service that runs python in the cloud for you.

url_to_submit = 'https://web.archive.org/save/https://d20s4vd27d0hk0.cloudfront.net/'
response = requests.get(url_to_submit, headers = {'user-agent':'@{} goverment archiving bot'.format('@gapolbot')})
