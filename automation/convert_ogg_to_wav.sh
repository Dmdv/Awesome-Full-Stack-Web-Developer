# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Tue, 20th Dec 2016, T 17:07 +01:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: convert_ogg_to_wav.sh
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:27 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



# Convert wav audio to Ogg
#
# Author: Anas Aboureada anasaboureada.com

find *.ogg | while read file ; do
	ffmpeg -i "${file}" "${file%.*}.wav" < /dev/null
	done
