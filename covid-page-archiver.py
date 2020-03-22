#!/usr/bin/python3

import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs
from difflib import SequenceMatcher
import argparse
import schedule
import time

PAGE_URL = ""
TIME_TOLERANCE = 1
CHANGE_THRESHOLD = 10


def older_than_tolerance(last_stamp: str, tolerance=1):
    """
    :param last_stamp:
    :param tolerance: More than <tolerance> hours, return True; else False
    :return:
    """
    if tolerance is None:
        tolerance = 1
    stamp1 = datetime.strptime(last_stamp, "%Y%m%d%H%M%S")
    diff = datetime.utcnow() - stamp1
    if diff.seconds > (tolerance * 3660):  # tolerance in hours
        return True
    return False


def get_last_save(page_url):
    res = requests.get('http://archive.org/wayback/available?url={}'.format(page_url))
    if res and res.json().get('archived_snapshots').get('closest'):
        return res.json()['archived_snapshots']['closest']['timestamp'], res.json()['archived_snapshots']['closest'][
            'url']


def page_has_changed(page_url, latest_archived_page_url, tolerance=10):
    if tolerance is None:
        tolerance = 10
    tolerance = tolerance / 100  # convert 10% to .10
    current_html = bs(requests.get(page_url).content, features="lxml")
    old_html = bs(requests.get(latest_archived_page_url).content, features="lxml")
    if SequenceMatcher(None, current_html.text, old_html.text).ratio() < (1 - tolerance):
        return True
    return False


def archive(page_url):
    response = requests.get(page_url, headers={'user-agent': '@{} government archiving bot'.format('@gapolbot')})
    if response:
        return True
    return False


def format_url(page_url):
    if not page_url.startswith('http://') and not page_url.startswith('https://'):
        return 'http://' + page_url
    return page_url


def schedule_it(every_x_hours: int = 4):
    """
    :param every_x_hours: How often (in hours) to check for updates. Default: 4 hours
    :return:
    """
    if every_x_hours == 1:
        schedule.every(every_x_hours).minute.do(main)
    else:
        schedule.every(every_x_hours).minutes.do(main)
    print("Check scheduled for every {} hour(s) (time tolerance: {} hour(s), change threshold: {}%)".format(every_x_hours, TIME_TOLERANCE, CHANGE_THRESHOLD))
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    last_saved_timestamp, last_url = get_last_save(PAGE_URL)
    if last_saved_timestamp:
        if older_than_tolerance(last_stamp=last_saved_timestamp, tolerance=TIME_TOLERANCE):
            if page_has_changed(PAGE_URL, last_url, tolerance=CHANGE_THRESHOLD):
                if archive(PAGE_URL):
                    print("Page archived successfully.")
                else:
                    print("Page could not be archived.")
            else:
                print("Page has not changed.")
        else:
            print("Page has been recently archived.")
    else:
        print("Could not find page on Wayback Machine.")


def setup():
    global TIME_TOLERANCE, PAGE_URL, CHANGE_THRESHOLD
    parser = argparse.ArgumentParser()
    parser.add_argument('url_to_save', help="URL of webpage to save")
    parser.add_argument('-s', '--schedule', type=int, help="Automatically check every X hour(s)")
    parser.add_argument('-t', "--time_tolerance", type=int, help="Check page if last Wayback Machine version is more "
                                                                 "than X hours old")
    parser.add_argument('-c', '--change_threshold', type=float,
                        help='If current webpage is more than X percent different than the '
                             'archived version, re-archive the current version')
    args = parser.parse_args()
    if args.change_threshold:
        CHANGE_THRESHOLD = args.change_threshold
    if args.time_tolerance:
        TIME_TOLERANCE = args.time_tolerance
    PAGE_URL = format_url(args.url_to_save)
    if args.schedule:
        schedule_it(every_x_hours=args.schedule)
    else:
        main()


setup()
