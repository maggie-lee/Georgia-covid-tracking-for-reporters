#!/usr/bin/python3.6

import requests

# This is the most simple way to submit a page to the internet archive. It doesn't have a timer, it doesn't check when
# the page was last submitted to internet archive.

# To make this run, you'd set it up somewhere as a scheduled task. There are many ways to do that, these are only two:
# It could be as a cron task on your own computer, like run at 5 am and 5 pm:  0 5,17 * * * python /path_to/the_script.py
# But your computer has to be on for that. 
#
# I myself run it twice a day as a scheduled task on PythonAnywhere, a service that runs python in the cloud for you.

url_to_submit = 'https://web.archive.org/save/https://dph.georgia.gov/covid-19-daily-status-report'
response = requests.get(url_to_submit, headers = {'user-agent':'@{} goverment archiving bot'.format('@gapolbot')})
