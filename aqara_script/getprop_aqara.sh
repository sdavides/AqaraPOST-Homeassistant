apk -q add inetutils-telnet
( sleep 3; printf "root\n"; sleep 1; printf "clear\n"; sleep 1; printf "agetprop full\n"; sleep 1; ) | telnet 192.168.1.4 | sed '1,7d' | grep -v '#'| sed -e 's/\]: \[/" \: \"/g' | sed -e 's/\[/"/g' | sed -e 's/\]/"/g' |sed 's/^/,/'|  sed -e '$a}}' |sed  '1s/^./{"0":{/' | sed 's/"{"/{"/' |  sed -e 's/\"\}\"/\"\}/g' | sed -e 's/\}\"/}/g' > /config/aqara_script/getprop_aqara.js.tmp
jq  '.["0"]' /config/aqara_script/getprop_aqara.js.tmp  > /config/aqara_script/getprop_aqara.js && rm /config/aqara_script/getprop_aqara.js.tmp || echo error
