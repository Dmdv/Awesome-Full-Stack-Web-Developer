# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Tue, 20th Dec 2016, T 14:46 +01:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: convert fl64le pcm to s16le pcm.sh
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:27 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



find * | while read file ; do
	ffmpeg -f f64le -acodec pcm_f64le -i "${file}" -f s16le -acodec pcm_s16le "${file}.pcm" < /dev/null
	mv "${file}.pcm" "${file}"
	done
