# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Fri, 7th Oct 2016, T 17:00 +02:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: copy_without_nodemodules.sh
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:27 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



#!/usr/bin/env bash
echo ""
echo "------------------------------"
echo "copy all folder contents but not node_modules nor .git folders into another folder"
echo "------------------------------"
echo ""

for name in *; do
  if [[$name != "node_modules"] && [$name != ".git"]]; then
    cp "$HOME/Users/anas/projects/sharkfish-server-ubuntu/" "$name"
    echo "copying ...$name"
  fi
done
