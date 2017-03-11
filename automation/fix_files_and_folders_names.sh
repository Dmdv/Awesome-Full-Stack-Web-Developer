# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Fri, 23rd Dec 2016, T 16:11 +01:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: fix_files_and_folders_names.sh
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 15:16 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



#!/bin/bash
# Convert filenames to lowercase
# and replace characters recursively
#####################################

if [ -z $1 ];then echo Give target directory; exit 0;fi

find "$1" -depth| while read file ; do
        directory=$(dirname "$file")
        oldfilename=$(basename "$file")
        newfilename="$(echo "$oldfilename" | tr 'A-Z' 'a-z' | tr ' ' '_' | tr '-' '_' | sed 's/_-_/-/g')"
        if [ "$oldfilename" != "$newfilename" ] && [ "$oldfilename" != "READ_ME.md" ] || [ "$oldfilename" != "README.md" ]; then
                mv "$directory/$oldfilename" "$directory/$newfilename"
                echo ""${directory}/${oldfilename}" ---> "${directory}/${newfilename}""
        fi
        done
exit 0
