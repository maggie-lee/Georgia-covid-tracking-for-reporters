#!/usr/bin/python3.6

import requests

url_to_submit = 'https://web.archive.org/save/https://dph.georgia.gov/covid-19-daily-status-report'
response = requests.get(url_to_submit, headers = {'user-agent':'@{} goverment archiving bot'.format('@gapolbot')})
