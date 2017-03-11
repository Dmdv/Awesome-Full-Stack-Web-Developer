#! python3
# coding=utf-8
# bostad.py - Check bostad.stockholm.se fot suitable apartments and send the results in email and desktop notification

import datetime
import sys
import bs4
import os
import re
from urllib3 import PoolManager, Timeout
from pync import Notifier
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import TwilioRestClient
import json

if len(sys.argv) < 2:
    print('Usage: python bostad.py [daily | hourly | Bostadssnabben]')
    sys.exit()

service_type = sys.argv[1]

counters = {
    "New Production Apartments"    : 0,
    "Quick Apartments"             : 0,
    "Short Time Apartments"        : 0,
    "Student Apartments"           : 0,
    "Huge student queue Apartments": 0,
    "Youth Apartments"             : 0,
    "Old +55 Apartments"           : 0,
    "Old +65 Apartments"           : 0,
    "Old +75 Apartments"           : 0,
    "Suitable Apartments"          : 0
}

msg_txt = ''

cwd = '/Users/anas/projects/task_automation/'

with open(cwd + 'credentials.json') as data_file:
    credentials = json.load(data_file)

os.makedirs(cwd + "/bostad", exist_ok=True)
today = datetime.date.today()
today_date_str = today.strftime('%d, %b %Y')
today_file_path = os.path.join(cwd + '/bostad', os.path.basename(today_date_str))
open(os.path.join(cwd + '/bostad', os.path.basename(today_date_str)), 'w')


def print_counters():
    counters_txt = ''
    counters_txt += '\n<<<<<< {:^30} >>>>>>\n\n'.format('Counters')
    print('\n<<<<<< {:^30} >>>>>>\n\n'.format('Counters'))

    with open(os.path.join(cwd + '/bostad', os.path.basename(today_date_str)), 'a') as bostad_file:
        bostad_file.write('\n<<<<<< Counters >>>>>>\n')

        for counter_key in sorted(counters.keys()):

            print('{0: >30}:\t{1}\n'.format(counter_key, counters[counter_key]))

            bostad_file.write('{0: >30}:\t{1}\n'.format(counter_key, counters[counter_key]))

            counters_txt += ('{0: >30}: {1}\n'.format(counter_key, counters[counter_key]))

        print('------------------------------------\n')
        print('{0: >30}: {1}\n'.format('Total Available:', apartments_counter))

        bostad_file.write('------------------------------------\n')
        bostad_file.write('{0: >30}: {1}\n'.format('Total Available:', apartments_counter))

        counters_txt += '------------------------------------\n'
        counters_txt += ('{0: >30}: {1}\n'.format('Total Available:', apartments_counter))

    return counters_txt


def print_apartment_details(apartment):
    columns = apartment.select('td')
    apartment_msg_txt = ''

    with open(os.path.join(cwd + '/bostad', os.path.basename(today_date_str)), 'ab') as bostad_file:

        for col in columns:
            child_col_txt = ''

            if col.select(".hidden"):
                break
            else:
                if len(list(col.children)) > 0:

                    if col.a:
                        print('{:^60}'.format(url + col.a.get('href')), end=' , ')
                        bostad_file.write(bytearray(('{:^60}'.format(url + col.a.get('href')) + ' , ').encode('utf-8')))

                        apartment_msg_txt += '{:^60}'.format(url + col.a.get('href') + ' , ')

                    for col_itr in col.children:
                        # print('col ' + str(col_itr.string).strip() + '\n')
                        if len(str(col_itr.string).strip()) > 0 and (
                            str(col_itr.string).strip() not in ['True', "b''", "False"]) and (
                            str(col_itr.string).strip().find('bostäder i samma annons') == -1) and (
                            str(col_itr.string).strip().find('bostaden är ny') == -1) and (
                            str(col_itr.string).strip().find('None Nyproduktion') == -1):
                            child_col_txt += str(col_itr.string).strip() + ' '
                        else:
                            continue
                    if len(child_col_txt) > 0:
                        print('{!s:^30}'.format(child_col_txt.encode('utf-8')), end=' ')
                        bostad_file.write(bytearray(('{!s:^30}'.format(child_col_txt).encode('utf-8'))))
                        apartment_msg_txt += '{!s:^30}'.format(child_col_txt)
                else:
                    child_col_txt += col.get_text()

                    if len(child_col_txt.strip()) > 0:
                        print(child_col_txt.strip(), end=' ')
                        bostad_file.write(bytearray((child_col_txt.strip() + ' ').encode('utf-8')))
                        apartment_msg_txt += (child_col_txt.strip() + ' ').encode('utf-8')

                if len(child_col_txt.strip()) > 0:
                    print('', end=' , ')
                    bostad_file.write(bytearray(' , '.encode('utf-8')))
                    apartment_msg_txt += ' , '

        print()
        print('\n{:-^300}\n'.format(''))
        bostad_file.write(bytearray('\n{:-^300}\n'.format('').encode('utf-8')))
        apartment_msg_txt += '\n{:-^300}\n'.format('')

    return apartment_msg_txt


def send_mail(to, frm, subject, email_txt):
    msg_body = MIMEMultipart('alternative')
    msg_body['Subject'] = subject
    msg_body['From'] = frm
    msg_body['To'] = to

    if email_txt:
        part = MIMEText(email_txt)
        msg_body.attach(part)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()

    s.login(credentials["gmail"]["email"], credentials["gmail"]["password"])

    s.sendmail(frm, to, msg_body.as_string())
    s.quit()


def send_sms(to_phone_no, sms_text):
    account_sid = credentials["twilio"]["account_sid"]
    auth_token = credentials["twilio"]["auth_token"]

    client = TwilioRestClient(account_sid, auth_token)

    client.messages.create(
            to=to_phone_no,
            from_="+15005550006",
            body=sms_text,
    )


email_title = 'Bostad Report - ' + today_date_str
http = PoolManager()
url = 'http://bostad.stockholm.se'
browse_url = "/Lista/?minRooms=0&maxRooms=6&minSpace=0&maxSpace=10&minRent=0&maxRent=9&areas=&sc=6&sd=desc"
res = http.request("GET", (url + browse_url), timeout=Timeout(connect=1.0, read=2.0))

now = datetime.datetime.now()
now_str = now.strftime('%d, %b %Y - %X ')
print(now_str, end=' :: ')
print("Downloading the page {0}".format(url + browse_url))
print('..............')

html = bs4.BeautifulSoup(res.data, "html.parser")
apartment_list = html.select("table.objlist tbody tr")
apartments_counter = len(apartment_list)

if service_type == 'Bostadssnabben':
    for apartment in apartment_list:

        new_production = apartment.findAll(text=re.compile('^Nyproduktion'))
        quick = apartment.findAll(text=re.compile('^Bostadssnabben'))
        short_time = apartment.findAll(text=re.compile('^Korttid'))
        student = apartment.findAll(text=re.compile('^Student'))
        huge_student = apartment.findAll(text=re.compile('^Huge studentkö'))
        youth = apartment.findAll(text=re.compile('^Ungdom'))
        old_75 = apartment.findAll(text=re.compile('^Trygghetsboende Stockholm'))
        old_65 = apartment.findAll(text=re.compile('^65+'))

        if quick:
            if not (short_time or student or huge_student or youth or old_65):
                print('*/*/*/*/*//*/*/*/*/*/*/*/*/ Bostadssnabben */*/*/*//*/*/*/*/*/*/*/')
                Notifier.notify('Bostad Bostadssnabben!!!!', title='Bostad')
                email_title += ' -  Bostadssnabben found!!!'
                counters["Suitable Apartments"] += 1
                counters["Quick Apartments"] += 1
                msg = print_apartment_details(apartment)
                counters_msg_txt = print_counters()
                msg += counters_msg_txt
                send_mail('Anas <anas.ieee@gmail.com>',
                          'Bostad Report <AnasFullStack@AnasFullStack.com>',
                          email_title,
                          msg)
            continue
    exit(0)

elif service_type == 'daily':
    for apartment in apartment_list:

        new_production = apartment.findAll(text=re.compile('^Nyproduktion'))
        quick = apartment.findAll(text=re.compile('^Bostadssnabben'))
        short_time = apartment.findAll(text=re.compile('^Korttid'))
        student = apartment.findAll(text=re.compile('^Student'))
        huge_student = apartment.findAll(text=re.compile('^Huge studentkö'))
        youth = apartment.findAll(text=re.compile('^Ungdom'))
        old_75 = apartment.findAll(text=re.compile('^Trygghetsboende Stockholm'))
        old_65 = apartment.findAll(text=re.compile('^65+'))
        old_55 = apartment.findAll(text=re.compile('^55+'))

        if new_production:
            if not (short_time or student or huge_student or youth or old_75 or old_65 or old_55):
                print('\n{0:*^300}\n'.format('Nyproduktion'))
                Notifier.notify('Bostad Nyproduktion!!!!', title='Bostad')
                counters["Suitable Apartments"] += 1
                counters["New Production Apartments"] += 1
                email_title += ' - Nyproduktion found!!!'
                msg_txt += ('\n{:*^300}\n'.format('Nyproduktion'))
                msg_txt += print_apartment_details(apartment)
                msg_txt += ('\n{:*^300}\n'.format(''))
            continue

        elif quick:
            if not (short_time or student or huge_student or youth or old_75 or old_65 or old_55):
                print('*/*/*/*/*//*/*/*/*/*/*/*/*/ Bostadssnabben */*/*/*//*/*/*/*/*/*/*/')
                Notifier.notify('Bostad Bostadssnabben!!!!', title='Bostad')
                email_title += ' -  Bostadssnabben found!!!'
                counters["Suitable Apartments"] += 1
                counters["Quick Apartments"] += 1
                msg_txt += ('\n{:*^300}\n'.format('Bostadssnabben'))
                msg_txt += print_apartment_details(apartment)
                msg_txt += ('\n{:*^300}\n'.format(''))

            continue

        elif short_time:
            counters["Short Time Apartments"] += 1
            # print('*/*/*/*/*//*/*/*/*/*/*/*/*/ Korttid */*/*/*//*/*/*/*/*/*/*/')
            continue

        elif student:
            counters["Student Apartments"] += 1
            # print('*/*/*/*/*//*/*/*/*/*/*/*/*/ Student */*/*/*//*/*/*/*/*/*/*/')
            continue

        elif huge_student:
            counters["Huge student queue Apartments"] += 1
            # print('*/*/*/*/*//*/*/*/*/*/*/*/*/ Huge studentkö */*/*/*//*/*/*/*/*/*/*/')
            continue

        elif youth:
            counters["Youth Apartments"] += 1
            # print('*/*/*/*/*//*/*/*/*/*/*/*/*/ Ungdom */*/*/*//*/*/*/*/*/*/*/')
            continue

        elif old_75:
            counters["Old +75 Apartments"] += 1
            # print('*/*/*/*/*//*/*/*/*/*/*/*/*/ Trygghetsboende Stockholm */*/*/*//*/*/*/*/*/*/*/')
            continue

        elif old_65:
            counters["Old +65 Apartments"] += 1
            # print('*/*/*/*/*//*/*/*/*/*/*/*/*/ 65+ */*/*/*//*/*/*/*/*/*/*/')
            continue

        elif old_55:
            counters["Old +55 Apartments"] += 1
            # print('*/*/*/*/*//*/*/*/*/*/*/*/*/ 65+ */*/*/*//*/*/*/*/*/*/*/')
            continue

        else:
            counters["Suitable Apartments"] += 1
            msg_txt += print_apartment_details(apartment)

    counters_msg_txt = print_counters()
    msg_txt += counters_msg_txt

    send_mail('Anas <anas.ieee@gmail.com>',
              'Bostad Report <AnasFullStack@AnasFullStack.com>',
              email_title,
              msg_txt)

    exit(0)
