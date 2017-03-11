# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Mon, 14th Nov 2016, T 09:54 +01:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: remove_ds_store.sh
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:26 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



#!/bin/bash
# Remove DS_Store file from folder recursevly
#####################################

if [ -z $1 ];then echo Give target directory; exit 0;fi

find "$1" -depth| while read file ; do
        directory=$(dirname "$file")
        filename=$(basename "$file")
        if  [ "$filename" == ".DS_Store" ] ||  [ "$filename" == ".ds_store" ] ; then
                rm "$directory/$filename"
                echo "removing $directory/$filename"
        fi
        done
exit 0
