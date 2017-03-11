#! python3
# coding=utf-8
# bostad.py - Check bostad.stockholm.se fot suitable apartments and send the results in email and desktop notification

import random
import datetime
import sys
import re
import bs4
import urllib3
import urllib
from pync import Notifier
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

urllib3.disable_warnings()

def load_user_agent(uafile):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1 - 1])
    random.shuffle(uas)
    return uas


# def main():
#     cwd = "/Users/anas/projects/main_private_repo/task_automation/"
#
#     user_agents = load_user_agent(uafile=cwd + "user_agents")
#     header = {
#         "ACCEPT": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#         "ACCEPT_ENCODING": "gzip, deflate, sdch, br",
#         "CACHE_CONTROL": "max-age=0",
#         "Connection": "close",
#         "User-Agent": user_agents[0].decode("utf-8"),
#         "ACCEPT_LANGUAGE": "en-US,en;q=0.8,de-DE;q=0.6,de;q=0.4,ar;q=0.2,fr;q=0.2"
#     }
#
#     http = urllib3.PoolManager(10, headers=header)
#     base_url = "http://womsa.se/"
#     browse_url = '/teckensomstod'
#     main_page = http.request("GET", (base_url + browse_url), timeout=urllib3.Timeout(connect=5.0, read=20.0))
#
#     categories = bs4.BeautifulSoup(main_page.data, "html.parser").findAll("li", {"class": "cat-item"})
#     categories_urls = []
#     categories_names = []
#     dropbox_urls = []
#
#     with open ('dropbox2.txt', 'a') as f:
#
#         for category in categories:
#             categories_urls.append(category.a['href'])
#             categories_names.append(category.a.get_text())
#
#         for categories_url in categories_urls:
#             catPage = http.request("GET", categories_url, timeout=urllib3.Timeout(connect=10.0, read=50.0))
#             regex = re.compile('https://www.dropbox.com/.*')
#
#             catUrls = bs4.BeautifulSoup(catPage.data, "html.parser").findAll("a", href=regex)
#
#             for drop_url in catUrls:
#                 print(drop_url['href'])
#                 dropbox_urls.append(drop_url['href'])
#                 f.write(drop_url['href'])
#                 f.write("\n")
#
#     f.close()
#
#     exit(0)

def main():
    cwd = "/Users/anas/projects/main_private_repo/task_automation/"

    user_agents = load_user_agent(uafile=cwd + "user_agents")
    header = {
        "ACCEPT": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "ACCEPT_ENCODING": "gzip, deflate, sdch, br",
        "CACHE_CONTROL": "max-age=0",
        "Connection": "close",
        "User-Agent": user_agents[0].decode("utf-8"),
        "ACCEPT_LANGUAGE": "en-US,en;q=0.8,de-DE;q=0.6,de;q=0.4,ar;q=0.2,fr;q=0.2"
    }

    http = urllib3.PoolManager(10, headers=header)
    urls = []

    with open('dropbox2.txt.unique', 'r') as drps:
        urls =  drps.read().splitlines()

    print(urls)

    for url_ in urls:
        main_page = http.request("GET", url_, timeout=urllib3.Timeout(connect=5.0, read=20.0))
        print(main_page)

        data = bs4.BeautifulSoup(main_page.data, "html.parser")

        file_name = url_[url_.rindex('/'): url_.index('?')]
        print('downloading ' + file_name+ ' ...')

        with open(cwd + '/swedish' + file_name, "wb") as f :
            f.write(data)
            f.close()

    exit(0)


if __name__ == "__main__":
    main()
