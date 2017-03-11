#!/usr/local/bin/python3
# coding=utf-8

import os
import csv
import re
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
hr_keywords = ['.* hr .*', '.*recruitment.*', '.*recruiter.*', '.*opportunity.*', '.*available.*', '.*seeking.*',
               '.*candidate.*']
combined_hr_regex = "(" + ")|(".join(hr_keywords) + ")"
emails = []

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


def get_hr_emails():
    connections_path = '../../data_science/data_sets/Complete_LinkedInDataExport_10-21-2016/Connections.csv'

    with open(connections_path) as connections_file:
        connections = csv.DictReader(connections_file)
        for row in connections:
            if (re.match(combined_hr_regex, row['Current Position'].lower())) or (
                    re.match(combined_hr_regex, row['Current Company'].lower())):
                emails.append(row)


def get_contacted_me_emails():
    inbox_path = '../../data_science/data_sets/Complete_LinkedInDataExport_10-21-2016/inbox.csv'
    with open(inbox_path) as inbox_file:
        inbox = csv.DictReader(inbox_file)
        for row in inbox:
            if (re.match(combined_hr_regex, row['Content'].lower())) or (
                    re.match(combined_hr_regex, row['Subject'].lower())):
                print(row)
                email_found = re.findall(r'[\w\.-]+@[\w\.-]+', str(row))
                if (len(email_found) > 0):
                    email_from = row['To'] if row['From'] == "Anas AbouReada" else  row['From']
                    new_email = {"Email Address": email_found[0], "First Name": email_from}
                    emails.append(new_email)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html(emails):
    fname = "index.html"
    context = {
        'emails': emails
    }

    with open(fname, 'w') as f:
        html = render_template('index.template.html', context)
        f.write(html)


def main():
    get_hr_emails()
    get_contacted_me_emails()
    create_index_html(emails)


if __name__ == "__main__":
    main()
