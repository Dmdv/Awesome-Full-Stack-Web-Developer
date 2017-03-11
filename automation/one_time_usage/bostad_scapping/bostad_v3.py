#! python3
# coding=utf-8
# bostad.py - Check bostad.stockholm.se fot suitable apartments and send the results in email and desktop notification

import random
import datetime
import sys
import bs4
import urllib3
from pync import Notifier
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

urllib3.disable_warnings()


def fire_usage_error():
    print("Usage: python bostad.py [Nyproduktion | Vanlig | Bostadssnabben]")
    sys.exit()


def send_mail(to, frm, subject, email_txt, credentials):
    msg_body = MIMEMultipart("alternative")
    msg_body["Subject"] = subject
    msg_body["From"] = frm
    msg_body["To"] = to

    if email_txt:
        part = MIMEText(email_txt)
        msg_body.attach(part)

    s = smtplib.SMTP("smtp.gmail.com:587")
    s.ehlo()
    s.starttls()

    s.login(credentials["gmail"]["email"], credentials["gmail"]["password"])

    s.sendmail(frm, to, msg_body.as_string())
    s.quit()


def get_apartments_details(apartments_list, base_url):
    apartments_details = ""

    for apartment in apartments_list:
        apartment_row = ""
        adjectives = ""
        print([tag.attrs for tag in bs4.BeautifulSoup(str(apartment), "html.parser")])

        # apartment_adjectives = apartment.select(".egenskapsrad .egenskap")
        # for adj in apartment_adjectives:
        #     adj_text = bs4.BeautifulSoup(str(adj), "html.parser")
        #     adj = adj_text.select(".egenskap")[0].text.strip()
        #     adjectives += "{0:^13}".format(adj)
        #
        # area = "{0:^40}".format(apartment.select(".adressinfo .omrade")[0].text)
        # street = "{0:^40}".format(apartment.select(".adressinfo .gatuadress")[0].text)
        # adress_info = apartment.select(".adressinfo")[0]
        # link = base_url + str(adress_info.get("href")) + "   "
        # # announce_till = apartment.select(".inforad div")[0].text.strip()[14:]
        #
        # apartment_row += area + street + adjectives + link
        #
        # apartments_details += apartment_row + "\n\n"

    return apartments_details


def load_user_agent(uafile):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1 - 1])
    random.shuffle(uas)
    return uas


def main():
    if len(sys.argv) < 2:
        fire_usage_error()

    service_type = sys.argv[1]
    cwd = "/Users/anas/projects/main_private_repo/automation/"

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
    base_url = "https://bostad.stockholm.se"
    browse_url = '/lista'
    res = http.request("GET", (base_url + browse_url), timeout=urllib3.Timeout(connect=1.0, read=2.0))

    now = datetime.datetime.now()
    now_str = now.strftime("%d, %b %Y - %X ")
    print(now_str, end=" :: ")
    print("Downloading the page {0}".format(base_url + browse_url) + ' - ' + service_type)
    print("..............")


    type_attr = "data-lagenhetstyp-" + service_type.lower()
    apartments_list = bs4.BeautifulSoup(res.data, "html.parser").find_all('a', {type_attr: "True", "class": 'm-apartment-card'})
    print(len(apartments_list))

    if len(apartments_list) > 0:
        apartments_details = get_apartments_details(apartments_list, base_url)

        Notifier.notify("Bostad " + service_type + " " + str(len(apartments_list)), title="Bostad")

        today = datetime.date.today()
        today_date_str = today.strftime("%d, %b %Y")
        with open(cwd + "credentials.json") as cred:
            credentials = json.load(cred)
        email_title = service_type + " - Bostad Report - " + today_date_str

        send_mail("Anas <anas.ieee@gmail.com>",
                  "Bostad Report <AnasFullStack@AnasFullStack.com>",
                  email_title,
                  str(apartments_details),
                  credentials)
    exit(0)


if __name__ == "__main__":
    main()
