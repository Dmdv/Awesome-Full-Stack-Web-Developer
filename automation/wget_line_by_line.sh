# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Mon, 14th Nov 2016, T 10:00 +01:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: wget_line_by_line.sh
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:26 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



#!/usr/bin/env bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    wget $line  -P ~/projects/anas/code/automation/scrap_imdb_movies_pics/posters/ &
done < "$1"
