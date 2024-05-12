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
* Use BurpSuite or ZAP or similar:
	* Follow [BurpSuite Guide](https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/Burp%20Suite%20Guide.pdf)
 	* Follow [ZAP Guide](https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/ZAP%20Guide.pdf)
         * [free dowload](https://www.zaproxy.org/download)
	* Download [AqaraHome apk mod](https://drive.google.com/file/d/1Wfn_ynyCGvPwldjbbNGvZmYBKj5csuMy/view?usp=sharing)
 
## Why? ##
I have an Aqara Hub G3 camera on HomeAssistant but I can't control it, with the homekit connection I only have the alarm function.

## Info ##
This is the beauty of it: no modifications to the device are necessary.

You can delete AqaraHome_mod app it without logging out, otherwise the token values ​​​​are expired.

AqaraHome apk mod includes acceptance of the user-installed certificate, (to see the http requests in burp)


## Install OK ##
![319800579-a36eb9e9-8a0c-480c-82db-3def3f8d51a9](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/2ea10616-0af3-4a10-84f7-d5cebd9b0435)


## Update data ##
* add automation every 1 minute:

	  
		description: Update Aqara G3
		mode: single
		trigger:
 		 - platform: time_pattern
 		   minutes: /1
		condition: []
		action:
		  - service: button.press
		    metadata: {}
		    data: {}
		    target:
		      entity_id: button.camera_g3_log
	  
or change inject node:

![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/ebf6ebad-bdb0-427e-add6-d8a3dcb8caa6)

## Update flow ##

for a successful update of the existing flow without changing the entities in HomeAssistant, follow the steps:
  * import new json
    
    ![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/75ce29e0-e829-417c-bd2c-0db5ced8199a)

  * delete old flow (complete flow card)

![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/b7db7bc7-5a7a-4fc9-bd1b-1899e8977b5a)

  * deploy  
!! do not deploy without deleting the old !!


---

## TIPS Hub G3 ##
* HomeKit for alarm function:
    * autodiscovery, insert qrcode number
    
  (port change every reboot of device, find with nmap
  replace into "/config/.storage/core.config_entries")

  ![4](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/f26c6a0c-6b96-4c41-b0ce-50332f542e87)

---

* Live video:
   * hack G3 (delete authentication rtsp):
     * Manual downgrade firmware [3.3.4](https://github.com/niceboygithub/AqaraCameraHubfw/blob/main/stock/G3) (post_init.sh enable)
     * Open telnet QR method [aQRootG3](https://github.com/Wh1terat/aQRootG3) (create post_init.sh)
     * Manual update firmware [3.3.9](https://github.com/niceboygithub/AqaraCameraHubfw/blob/main/stock/G3) (post_init.sh enable)
     * Update last firmware from command [custom firmware](https://github.com/niceboygithub/AqaraCameraHubfw/tree/main/modified/G3#flash-g3-custom-firmware-method)
         * hack done! (post_init.sh enable)
     * Add /data/scripts/post_init.sh from telnet
        ```
		killall -9 rtsp && rtsp >/dev/null 2>&1 &
		```
          or you can see rtsp user/pass (change every boot)

          from telnet command:
	  	```bash
	  	agetprop sys.camera_rtsp_url  # agetprop full (list all prop.)
	  	```
	  	![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/f4a401f3-f9f0-4fd3-a9f8-ea8605c8bba9)


	 	 rtsp://192.168.1.52:8554/360p (/720p /1080p /1296p)

	 	 rtsp://USER:PASS@192.168.1.52:8554/360p (/720p /1080p /1296p)

---

## See also ##

[go2rtc](https://github.com/AlexxIT/go2rtc) RTSP Proxy (HomeKit supported)
     
[WebRTC](https://github.com/AlexxIT/WebRTC) Card RTSP 

[AqaraCameraHubfw](https://github.com/niceboygithub/AqaraCameraHubfw) HACK 

[m3u8-HLS-Homeassistant](https://github.com/sdavides/m3u8-HLS-Homeassistant/)

[EPGItaly-Homeassistant](https://github.com/sdavides/EPGItaly-Homeassistant/)
