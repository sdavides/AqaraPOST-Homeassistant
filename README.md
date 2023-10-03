Goal: Replace Post request "Aqara Home" app on HomeAssistant


- Requirement:

NodeRed on HomeAssistant

NodeRed Companion on HomeAssistant

Palette "node-red-contrib-config" for NodeRed

Access internet from HomeAssistant server (for aqara URL https)

Aqara mod network.apk
https://drive.google.com/file/d/1Wfn_ynyCGvPwldjbbNGvZmYBKj5csuMy/view?usp=sharing

---

- Your value from BurpSuite on “config" node in to NodeRed:

appid	(XXXXXXAPPIDXXXXXXXXXXX)

userid	(XXXXXXUSERID.USERIDXXXXXXXXXXX)

token	(XXXXXXTOKENXXXXXXXXXXX)

aqara_url	(example EU = rpc-ger.aqara.com )

lumi1.54ef443a120c (example for Aqara G3 EU)

---

- Requirement for BurpSuite:

Install BurpSuite https://github.com/SNGWN/Burp-Suite

Install “Aqara Home” mod network on Android Phone

Install your certificate BurpSuite on Android Phone

Set proxy ip on Android Phone wifi with BurpSuite software

---

- Result

![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/92e05aa3-8dd3-4257-9c3b-ccc84f4e65d8)
![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/316750b5-7ddb-4539-a2b8-c157d262215c)

