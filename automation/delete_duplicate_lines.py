# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Thu, 6th Oct 2016, T 10:38 +02:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: delete_duplicate_lines.py
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:26 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



#!/usr/local/bin/python3

import sys
import codecs

if (len(sys.argv) < 2):
    print('Usage: python3 ./delete_duplicate_lines.py /path/to/target/file')
    sys.exit(1)

def uniquelines(lineslist):
    unique = {}
    result = []
    for item in lineslist:
        if item.strip() in unique: continue
        unique[item.strip()] = 1
        result.append(item)
    return result

file1 = codecs.open(sys.argv[1],'r+','cp1251')
filelines = file1.readlines()
file1.close()

with codecs.open(sys.argv[1] + ".unique", "w", "cp1251") as output:
    output.writelines(uniquelines(filelines))
