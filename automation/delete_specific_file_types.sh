# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Sat, 11th Mar 2017, T 15:17 +01:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: delete_specific_file_types.sh
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 15:31 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



#!/bin/bash

if [ -z $1 ];then echo Give target directory; exit 0;fi

find "$1" -depth| while read file ; do
        if  [ ${file: -3} != ".py" ] && [ ${file: -4} != ".cpp" ];then
                rm -f "$file"
                echo "Removed" ${file}
        fi
        done

find "$1" -type d -empty -delete
exit 0
