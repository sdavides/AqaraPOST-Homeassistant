Goal: Replace Post request "Aqara Home" app on HomeAssistant

-  this flow is example and was developed for Aqara Hub G3 camera (CH-H03 lumi.camera.gwpgl1)

---

- Requirement appid - userid - token

Find your value from BurpSuite, replace your value:

- https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/Burp%20Suite%20Guide.pdf

appid	(XXXXXXAPPIDXXXXXXXXXXX)

userid	(XXXXXXUSERID.USERIDXXXXXXXXXXX)    (autoconfig "userid" value, enter manual if not work)

token	(XXXXXXTOKENXXXXXXXXXXX)

aqara_url	( example EU = rpc-ger.aqara.com )

lumi1.XXXXXXXXXXXX ( lumi1.MACADDRESS )

---

- Requirement for find your data on BurpSuite software:

Install BurpSuite Software PC

Install “Aqara Home” mod network apk on Android Phone

Aqara 4.0.2_mod_network.apk or Aqara 3.0.6_mod_network.apk

( https://drive.google.com/file/d/1Wfn_ynyCGvPwldjbbNGvZmYBKj5csuMy/view?usp=sharing )

Install your certificate BurpSuite on Android Phone

Set proxy on Android Phone wifi with IP PC BurpSuite

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
