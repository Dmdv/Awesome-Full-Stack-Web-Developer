# @Author: Anas Aboureada <AnasAboureada>
# @Date:   Tue, 20th Dec 2016, T 14:46 +01:00
# @Email:  me@anasaboureada.com
# @Project: awesome-full-stack-web-developer
# @Filename: convert_wav_to_pcm.sh
# @Last modified by:   AnasAboureada
# @Last modified time: Sat, 11th Mar 2017, T 14:27 +01:00
# @License: MIT License
# @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>



find *.wav | while read file ; do
	ffmpeg -i "${file}" -f s16le -acodec pcm_s16le "${file%.*}.pcm" < /dev/null
	done
