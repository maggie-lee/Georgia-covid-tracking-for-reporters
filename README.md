# Georgia-covid-tracking-for-reporters
Reporter resources for tracking covid-19 in Georgia

The Georgia Department of Public Health is publishing a daily COVID-19 status report:
 
[https://dph.georgia.gov/covid-19-daily-status-report](https://dph.georgia.gov/covid-19-daily-status-report)

#### Archived copies of the state page

If you want to track changes over time in the number of tests or number of cases, you can get archived copies of earlier versions of the state page at the Internet Archive's Wayback Machine.

It looks like several bots are archiving the state's page every couple of hours. So you can see [archived copies of the state page.](https://web.archive.org/web/*/https://dph.georgia.gov/covid-19-daily-status-report)

I started running one myself March 18. Its that file above, covid-page-archiver-simple.py. It'll archive the state page two or three times a day or so.

UPDATE March 23: All the high fives to [Nate Harris](https://github.com/nwithan8) for writing like a do-it-all version of this archiver with scheduling, command-line arguments, fine controls.

All that is in covid-page-archiver.py and requirements.txt above and in [Nate's Github](https://github.com/nwithan8/Georgia-covid-tracking-for-reporters).  🙏

#### Changes to the page

If you want an alert for changes to the page and are not into coding, I'd recommend [Distill.io](https://www.distill.io) BUT the free tier only checks every six hours.
If you want more frequent checks, I'm not aware of any free service to do that, but the Distill paid tier will do it, and probably some other sites would too.


