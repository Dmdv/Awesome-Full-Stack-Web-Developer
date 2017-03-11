# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Mon, 19th Sep 2016, T 12:09 +02:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: parse_json.py
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:26 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



#!/usr/local/bin/python3

import sys
import json

if (len(sys.argv) < 2):
    print('Usage: python3 ./parse_json.py json_data_filename.json')
    sys.exit(1)

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)
    modus_output = data['modusOutput']
    modus_output_parsed = json.loads(modus_output)

f = open('new_' + sys.argv[1], 'w')
f.write(str(modus_output_parsed))
f.close()

print ('"new_' + sys.argv[1] + '" is created successfully ;-)')
sys.exit(0)
