from urllib.request import urlopen
from bs4 import BeautifulSoup
from pync import Notifier
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json


print("--------------------------- Starting migrationsverket cron job---------------------------------------")
html_content = urlopen(
        "http://www.migrationsverket.se/Kontakta-oss/Kontrollera-din-ansokan/Utan-inloggning.html?typenr=2&q=54654486"
        "&submitButton=S%C3%B6k")
# html_content = urlopen(
#         "http://www.migrationsverket.se/Kontakta-oss/Kontrollera-din-ansokan/Utan-inloggning.html?typenr=1&q=50303456"
#         "&submitButton=S%C3%B6k")
html_obj = BeautifulSoup(html_content.read(), "html.parser")
success_box = html_obj.findAll("div", {"class": "message-box successbox"})
warning_box = html_obj.findAll("div", {"class": "message-box warningbox"})


def send_mail(to, frm, subject, text, html):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = frm
    msg['To'] = to

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

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


if (success_box):
    print('WOOOOOOOOO case is closed')
    Notifier.notify('WOOOOOOOOO case is closed', title='Migrationsverket')
    send_mail('Anas <anas.ieee@gmail.com>',
              'Migrationsverket <AnasFullStack@AnasFullStack.com>',
              'Migrationsverket - WOOOOOOOOO case is closed',
              success_box[0].get_text(),
              success_box[0])
    exit(0)

else:
    if (warning_box):
        print('Yeeeeeeee not yet!!!!')
        Notifier.notify('Yeeeeeeee not yet!!!!', title='Migrationsverket')
        send_mail('Anas <anas.ieee@gmail.com>',
                  'Migrationsverket <AnasFullStack@AnasFullStack.com>',
                  'Migrationsverket - Yeeeeeeee not yet!!!!',
                  warning_box[0].get_text(),
                  warning_box[0])
        exit(0)
    else:
        print('Error')
        Notifier.notify('Errorrrrrrrrrrr!!!!', title='Migrationsverket')
        exit(1)
