# Georgia-covid-tracking-for-reporters
Reporter resources for tracking covid-19 in Georgia

Compiled by Maggie Lee

The Georgia Department of Public Health is publishing a daily COVID-19 status report:
 
[https://dph.georgia.gov/covid-19-daily-status-report](https://dph.georgia.gov/covid-19-daily-status-report)

If you want to track changes over time in the number of tests or number of cases, you can get archived copies of earlier versions of the state page at the Internet Archive's Wayback Machine. Several bots are tracking the state report page and periodically submitting the page to the Internet Archive. It's just snapshots of what the page looked like at various times in the past.

#### Archived copies of the state page from 04/28/20 to ???
[Archived copies of the daily Georgia COVID-19 status report starting April 28](https://web.archive.org/web/*/https://ga-covid19.ondemand.sas.com/).
On or about April 27, the state changed how it published the page again. So I had to adjust my archiving bot again. We'll see how it goes 
 🤔. Stay tuned

#### Archived copies of the state page from **03/30/2020 19:07:03 until about 4/27 but somewhat spotty**

[Archived copies of the daily Georgia COVID-19 status report starting late April 1.](https://web.archive.org/web/*/https://d20s4vd27d0hk0.cloudfront.net/).

On or about 3/27, the state changed how it publishes the page -- technically, the state put the data on an inset page. A viewer can't see the difference, but a robot can, and basically the robot needed a reset to tell it "pick up the inset page with the data." 

But I didn't realize that for a couple of days, so this method is missing some days.

On April 1, I started a bot to archive that inset page. That's the file covid-page-archiver-simple.py above. Some other bot was already archiving it too. 

#### Archived copies of the state page from 3/14/2020 to about 3/27/2020, 12:00pm

[Archived copies of the state page, volume 1.](https://web.archive.org/web/*/https://dph.georgia.gov/covid-19-daily-status-report)

Several bots were archiving this already when I started one on March 18. 

All the high fives to [Nate Harris](https://github.com/nwithan8) for writing like a do-it-all version of this archiver with scheduling, command-line arguments, fine controls. Like, you could use it to archive any page, not just the covid page.

All that is in covid-page-archiver.py and requirements.txt above and in [Nate's Github](https://github.com/nwithan8/Georgia-covid-tracking-for-reporters).  🙏

#### All the diagnosis numbers from every county from all the days

The New York Times is publishing data that shows cumulative counts of coronoavirus cases in every county in the U.S. Their data is at [NY Times Github](https://github.com/nytimes/covid-19-data).

#### Changes to the Georgia page

If you want an alert for changes to the page and are not into coding or the command line, I'd recommend [Distill.io](https://www.distill.io) BUT the free tier only checks every six hours.
If you want more frequent checks, I'm not aware of any free service to do that, but the Distill paid tier will do it, and probably some other sites would too.


