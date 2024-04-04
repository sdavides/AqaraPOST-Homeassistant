#  AqaraPOST-Homeassistant #

Goal: Replace Post request "Aqara Home" app on HomeAssistant

  * note: 
	* this flow is example and was developed for Aqara Hub G3 camera

## Requirement ##
* Your value from POST Request Aqara app:
  * appid  ( XXXXXXAPPIDXXXXXXXXXXX )
  * token ( XXXXXXTOKENXXXXXXXXXXX )
  * subjectId ( lumi1.XXXXXXXXXXXX ) usually MAC-ADDRESS
  * aqara url ( rpc-ger.aqara.com ) Host
    * [list aqara url](https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/generatejson/list_aqara_url.txt)
  * timezone ( it-IT ) -> es-ES/en-UK/de-DE/it-IT/pt-PT/en-US...
  * userid ( automatic, enter manual if not work )
	
## Method ##
* Method 1 NodeRed (recommended):
	* Import flow Aqara_G3_nodered.json 
	* Replace your value "config" node 
	* Deploy
		* note: you can use the script to generate your NoderRed json
		* [generatejson](https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/generatejson/README.md)
	
* Method 2 RestFul (without NodeRed):
	* Replace your value Aqara_G3_without_nodered.txt
	* Copy and paste Aqara_G3_without_nodered.txt on configuration.yaml
	* Restart HomeAssistant

 
## Find your Value ##
* Use BurpSuite or similar:
	* Follow [BurpSuite Guide](https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/Burp%20Suite%20Guide.pdf)
	* Download [AqaraHome apk mod](https://drive.google.com/file/d/1Wfn_ynyCGvPwldjbbNGvZmYBKj5csuMy/view?usp=sharing)
 
## Why? ##
I have an Aqara Hub G3 camera on HomeAssistant but I can't control it, with the homekit connection I only have the alarm function.

## Update flow ##

for a successful update of the existing flow without changing the entities in HomeAssistant, follow the steps:
  * import new json
    
    ![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/75ce29e0-e829-417c-bd2c-0db5ced8199a)

  * delete old flow (complete flow card)

![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/b7db7bc7-5a7a-4fc9-bd1b-1899e8977b5a)

  * deploy  
!! do not deploy without deleting the old !!

## Install OK ##
![0](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/54a22cd1-fdf8-4dc3-b2d4-a0e03d269cb4)
![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/a36eb9e9-8a0c-480c-82db-3def3f8d51a9)


---

## TIPS Hub G3 ##
* HomeKit for alarm function:
    * autodiscovery, insert qrcode number
    
     ( port change every reboot of device, scan and find with nmap

     replace port into "/config/.storage/core.config_entries" )

![4](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/f26c6a0c-6b96-4c41-b0ce-50332f542e87)

---

* Live video:
   * hack G3 (delete authentication rtsp):
     * open telnet [aQRootG3](https://github.com/Wh1terat/aQRootG3)
     * Firmware mod [firmware](https://github.com/niceboygithub/AqaraCameraHubfw/tree/main/modified/G3)
       * add post_init.sh: "killall -9 rtsp && rtsp >/dev/null 2>&1 &"
       
or you can see rtsp user/pass (change every boot)

from telnet command:
```bash
agetprop sys.camera_rtsp_url
```

rtsp://192.168.1.52:8554/360p (/720p /1080p /1296p)

rtsp://USER:PASS@192.168.1.52:8554/360p (/720p /1080p /1296p)

---

## See also ##

[go2rtc](https://github.com/AlexxIT/go2rtc) RTSP Proxy (HomeKit supported)
     
[WebRTC](https://github.com/AlexxIT/WebRTC) Card RTSP 

[AqaraCameraHubfw](https://github.com/niceboygithub/AqaraCameraHubfw) HACK 
