# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Mon, 3rd Oct 2016, T 14:44 +02:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: add_to_git_lfs.sh
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:27 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



#!/bin/bash

# Adding files with size > 2 Mb in a directory to git lfs
# Excluding node_modules and dist folders
################################################################

if [ -z "$1" ];then echo Give target directory; exit 0;fi

find "$1" -size +2000 | grep -v node_modules | grep -v dist| while read file ; do
        git lfs track "$file"
        done
exit 0
