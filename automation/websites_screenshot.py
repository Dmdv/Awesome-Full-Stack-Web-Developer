# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Sat, 18th Feb 2017, T 10:07 +01:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: websites_screenshot.py
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:26 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



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

display = Display(visible=0, size=(1200, 1200))
display.start()

browser = webdriver.Chrome()
browser.get('http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1')
browser.save_screenshot('screenie.png')
browser.quit()

display.stop()
