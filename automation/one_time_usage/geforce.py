from urllib.request import urlopen
from bs4 import BeautifulSoup
from pync import Notifier
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json


print("--------------------------- Starting geforce cron job---------------------------------------")
html_content = urlopen("http://www.geforce.com/hardware/10series/titan-x-pascal")
# html_content = urlopen("http://www.geforce.com/hardware/10series/geforce-gtx-1080")

html_obj = BeautifulSoup(html_content.read(), "html.parser")

out_of_stock = html_obj.findAll("div", {"class": "js-out-of-stock"})
hide_out_of_stock_with = out_of_stock[1].findAll("p", {"class": "js-out-of-stock__with-date", "style": "display: none;"})
hide_out_of_stock_without = out_of_stock[1].findAll("p", {"class": "js-out-of-stock__without-date", "style": "display: none;"})


def send_mail(to, frm, subject, text):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = frm
    msg['To'] = to

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()

    cwd = '/Users/anas/projects/main_private_repo/task_automation/'

    with open(cwd + 'credentials.json') as data_file:
        credentials = json.load(data_file)

    s.login(credentials["gmail"]["email"], credentials["gmail"]["password"])

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(frm, to, msg.as_string())
    s.quit()


if hide_out_of_stock_with and hide_out_of_stock_without:
    print('WOOOOOOOOO found geforce titan-x-pascal')
    Notifier.notify('WOOOOOOOOO found geforce', title='geforce')
    send_mail('Anas <anas.ieee@gmail.com>',
              'geforce <AnasFullStack@AnasFullStack.com>',
              'WOOOOOOOOO found geforce',
              'buy it now! http://www.geforce.com/hardware/10series/titan-x-pascal')
    exit(0)
else:
    print('geforce is not found')
    exit(0)
