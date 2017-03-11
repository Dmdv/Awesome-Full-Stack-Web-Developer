# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Sun, 30th Oct 2016, T 11:11 +01:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: generate_sequential_url.py
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:26 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



# coding=utf-8

import re

base_url = "http://www4.nok.se/laromedel/rivstart/01.mp3"
pattern = re.compile(r"\d+.mp3")

with open('rivstart_audio_urls.txt', 'w') as f:
    for i in range(1, 193):
        if (i < 10):
            f.write(pattern.sub('0' + str(i) + '.mp3', base_url))

        else:
            f.write(pattern.sub(str(i) + '.mp3', base_url))
        f.write('\n')
    f.close()
