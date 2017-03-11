# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Mon, 19th Dec 2016, T 20:11 +01:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: clone_all_bitbucket_repos.py
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:27 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



# Download all person's bitbucket repos
#
# Author: Anas Aboureada anasaboureada.com
##################################################

import sys
from subprocess import call
import requests

account_name = sys.argv[1]
repos = requests.get("https://api.bitbucket.org/1.0/users/%s" % account_name).json()

for repo in repos['repositories']:
    repo_name = repo['name']
    repo_url = "https://bitbucket.org/%s/%s" % (account_name, repo_name.lower())

    call(["git", "clone", repo_url])
