# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Sun, 5th Feb 2017, T 17:14 +01:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: create_test_cases.py
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 11:43 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



import sys
import random

items_count = 100000
max_item_value = 1000000000

with open ('./test_cases.txt', 'w') as f:
    f.write(items_count + '\n')
    for i in range(items_count):
        f.write(str(random.randint(0, max_item_value))+ ' ')
