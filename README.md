Goal: Replace Post request "Aqara Home" app on HomeAssistant

- Requirement appid - userid - token value

note:  this flow is example and was developed for Aqara Hub G3 camera (CH-H03 lumi.camera.gwpgl1)

---

Find your value from BurpSuite, replace your value:

- https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/Burp%20Suite%20Guide.pdf

appid	(XXXXXXAPPIDXXXXXXXXXXX)

userid	(XXXXXXUSERID.USERIDXXXXXXXXXXX)    (autoconfig "userid" value, enter manual if not work)

token	(XXXXXXTOKENXXXXXXXXXXX)

aqara_url	( example EU = rpc-ger.aqara.com )

lumi1.XXXXXXXXXXXX ( lumi1.MACADDRESS )

---

- Requirement for find your data on BurpSuite software:

BurpSuite Software PC

“Aqara Home” mod network apk on Android Phone

( https://drive.google.com/file/d/1Wfn_ynyCGvPwldjbbNGvZmYBKj5csuMy/view?usp=sharing )

---

- Method 1 RestFul (without NodeRed):

  1. Replace value Aqara_G3_without_nodered.txt

  2. Copy and paste Aqara_G3_without_nodered.txt on configuration.yaml

  3. Restart HomeAssistant

---

- Method 2 NodeRed (recommended):

  1. Install NodeRed on HomeAssistant (with "node-red-contrib-config" palette)

  2. Install NodeRed Companion on HomeAssistant

  3. Import flow Aqara_G3_nodered.json

  4. Replace value "config" node

  5. Deploy 

Note: access internet from HomeAssistant server (for aqara URL https)

---

---

- Result

![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/92e05aa3-8dd3-4257-9c3b-ccc84f4e65d8)
![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/316750b5-7ddb-4539-a2b8-c157d262215c)

---

---

- Trick for Hub G3:

Alarm function ->

  HomeKit device

  Warning: the port change every reboot of device. 

  Scan and find with nmap, replace port into "/config/.storage/core.config_entries"

![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/000112ab-1acf-4f88-b634-024df5a6c554)




Live video ->

go2RTC with WebRTC ( required HomeKit connected )

https://github.com/AlexxIT/go2rtc

https://github.com/AlexxIT/WebRTC


Update:
After many problems the best solution for live video:

hack G3:

- open telnet
  
- add post_init.sh:
  
  #delete auth rtsp
  
  sleep 40
  
  killall -9 rtsp
  
  rtsp >/dev/null 2>&1 &
  

- card with webrtc-camera url: rtsp://192.168.1.52:8554/360p /720p /1080p /1296p
  

