#!/bin/bash
# Ask the user details
echo "#"
echo "#"
echo "# This is is an automatic script to create the Node Red json HomeAssistant"
echo "# for the Aqara Hub G3, read on https://github.com/sdavides/AqaraPOST-Homeassistant "
echo "#"
echo "# save path /tmp/Aqara_G3_nodered.json"
echo "# first device"
echo "#"
echo "# See post request from Aqara app, example BurpSuite "
echo "#"
echo "# Replace your value XXXXXXTOKENXXXXXXXXXXX lumi1.XXXXXXXXXXXX: XXXXXXAPPIDXXXXXXXXXXX aqara_url"
echo "#"
echo "#"

echo "# Insert your token example: XXXXXXTOKENXXXXXXXXXXX"
read -p 'TOKEN : ' NEWTOKEN
echo "#"
echo "#"

echo "# Insert your lumi1 example: lumi1.XXXXXXXXXXXX"
read -p 'MAC lumi1.XXXXXXXXXXXX: ' NEWLUMI1
echo "#"
echo "#"

echo "# Insert your appid example: XXXXXXAPPIDXXXXXXXXXXX"
read -p 'APPID XXXXXXAPPIDXXXXXXXXXXX: ' NEWAPPID
echo "#"
echo "#"
curl -s https://raw.githubusercontent.com/sdavides/AqaraPOST-Homeassistant/main/generatejson/list_aqara_url.txt
echo "# Insert your aqara_url example: rpc-ger.aqara.com"
read -p 'URL aqara: ' aqara_url
echo "#"
echo "#"

echo "# Insert your country for timeformat example: es-ES/en-UK/de-DE/it-IT/pt-PT/en-US..."
read -p 'timezone: ' TIMEZONE
echo "#"
echo "#"
echo "# Your value: TOKEN:$NEWTOKEN LUMI1:$NEWLUMI1 APPID:$NEWAPPID AQARA_URL:$aqara_url"
echo "#"
echo "#"
echo "#"
echo "#"
echo "echo download last template" > /tmp/Aqara_G3_nodered.sh
echo "rm -rf /tmp/*Aqara_G3_nodered.json* && wget -q https://raw.githubusercontent.com/sdavides/AqaraPOST-Homeassistant/main/Aqara_G3_nodered.json --output-document=/tmp/tmp_Aqara_G3_nodered.json" >> /tmp/Aqara_G3_nodered.sh
echo "echo download complete" >> /tmp/Aqara_G3_nodered.sh
echo "echo insert value" >> /tmp/Aqara_G3_nodered.sh
echo "cat /tmp/tmp_Aqara_G3_nodered.json | sed -e 's/XXXXXXTOKENXXXXXXXXXXX/$NEWTOKEN/g' | sed -e 's/XXXXXXAPPIDXXXXXXXXXXX/$NEWAPPID/g' |sed -e 's/lumi1.XXXXXXXXXXXX/$NEWLUMI1/g' | sed -e 's/it-IT/$TIMEZONE/g' | sed -e 's/rpc-ger.aqara.com/$aqara_url/g' > /tmp/Aqara_G3_nodered.json" >> /tmp/Aqara_G3_nodered.sh
echo "echo insert complete" >> /tmp/Aqara_G3_nodered.sh

chmod +x /tmp/Aqara_G3_nodered.sh

echo "rm -rf /tmp/*tmp_Aqara_G3_nodered.json; rm -rf /tmp/*Aqara_G3_nodered.sh" >> /tmp/Aqara_G3_nodered.sh
echo "echo #" >> /tmp/Aqara_G3_nodered.sh
echo "echo complete, save path /tmp/Aqara_G3_nodered.json" >> /tmp/Aqara_G3_nodered.sh
echo "echo #" >> /tmp/Aqara_G3_nodered.sh
echo "rm -rf /tmp/*tmp_Aqara_G3_nodered.json; rm -rf /tmp/*Aqara_G3_nodered.sh ; rm -rf /tmp/AqaraPOST-Homeassistant* " >> /tmp/Aqara_G3_nodered.sh

/tmp/Aqara_G3_nodered.sh
