#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This script is for runnig on ubuntu

# First, install Google Chrome for Debian/Ubuntu:

sudo apt-get install libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome*.deb
sudo apt-get install -f

# Now, let’s install xvfb so we can run Chrome headlessly:

sudo apt-get install xvfb

# Install ChromeDriver:1

sudo apt-get install unzip

wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver

sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

# Install some Python dependencies and Selenium:

# Install pip:
sudo apt-get install python-pip

## (Optional) Create and enter a virtual environment:
# sudo apt-get install python-virtualenv
# virtualenv env
# source env/bin/activate

# Install Selenium and pyvirtualdisplay:
pip install pyvirtualdisplay selenium
'''

from pyvirtualdisplay import Display
from selenium import webdriver
import json
import re

display = Display(visible=0, size=(1200, 1200))
display.start()

browser = webdriver.Chrome()

regex = r".*\/title\/\s*([^\n\r]*\/)"


with open('./movie_metadata.json') as f:
    data = json.load(f)

for a in data:
    if 'movie_title' in a:
        title = a['movie_title']
    else:
        title = 'NoName'
    if 'movie_imdb_link' in a:
        m = re.match(regex, a['movie_imdb_link'])
        if m:
            groups = m.groups()
            movie_id = groups[0].encode('ascii','ignore')
            movie_id_fixed = movie_id[:-1]
            browser.get(a['movie_imdb_link'])
            screen_shoot_path = './images/' + movie_id_fixed + '_' + title + '.png'
            browser.save_screenshot(screen_shoot_path)
            print('New screen shoot saved to ' + screen_shoot_path)

browser.quit()
display.stop()
