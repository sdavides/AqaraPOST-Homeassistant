
#  AqaraPOST-Homeassistant addon #

Add-on for G3 camera or FP2 sensor
 
 * only Username/Password Aqara required
 	* the values ​​in the "config" node will be generated from the username and password if valid
 
 * [AqaraPost_[Node-RED]](https://github.com/sdavides/AqaraPOST-Homeassistant/tree/main/addon-AqaraPost/README.md)


----

----

#  AqaraPOST-Homeassistant #

Goal: Replace Post request "Aqara Home" app on HomeAssistant

  * note: 
	* this flow is example and was developed for Aqara G3 camera or FP2 sensor *( lumi1.xxxx )*

## Flow NodeRed ##

   1. [GenerateToken](https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/generatejson/README.md#generate-token-from-username-and-password)  username/password Aqara
      
        *thank you [Wh1terat](https://gist.github.com/Wh1terat/c4a4c665d692af461796e5eee9f5461d)*

   3. Import JSON on Node-Red
            
   4. Enter your values ​​in the "config" node:
      
      *Token, AppId, UserId, Lumi1, Area*

## Why? ##
I have an Aqara Hub G3 camera on HomeAssistant but I can't control it, with the homekit connection I only have the alarm function.

## Info ##
No modification to your device is required.

## Import flow NodeRed ##
![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/a7c093f9-c383-451d-b452-828d5d4b03af)
## Entity NodeCompanion ##
<img width="1346" height="1548" alt="immagine" src="https://github.com/user-attachments/assets/0b920251-d507-4bcf-bfda-5e7af7825387" />
<img width="838" height="558" alt="immagine" src="https://github.com/user-attachments/assets/27acc03b-9dcc-4bda-a508-750663d91338" />


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

---

## TIPS Hub G3 ##

* Turns the camera into an NGINX-cgi PHP server and much more...:
    * [AqaraG3-armv7-binary](https://github.com/sdavides/AqaraG3-armv7-binary)
      
      ![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/555c0f99-d010-4323-b365-070d26e4ad7f)

---

* HomeKit alarm function HomeAssistant:
    * autodiscovery, insert qrcode number
    
  		port change every reboot of device

      from telnet command:
	  	```bash
	  	netstat -anp|grep ha_master |grep ::: |awk '{print substr($4,1)}' | sed 's/::://'
	  	```
  		![4](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/f26c6a0c-6b96-4c41-b0ce-50332f542e87)

---

* Live video:
   * hack G3 (delete authentication rtsp):
     * Manual downgrade firmware [3.3.4](https://github.com/niceboygithub/AqaraCameraHubfw/blob/main/stock/G3) (post_init.sh enable)
     * Open telnet QR method [aQRootG3](https://github.com/Wh1terat/aQRootG3) (create post_init.sh)
     * Manual update firmware [3.3.9](https://github.com/niceboygithub/AqaraCameraHubfw/blob/main/stock/G3) (post_init.sh enable)
     * Update last firmware from command [custom firmware](https://github.com/niceboygithub/AqaraCameraHubfw/tree/main/modified/G3#flash-g3-custom-firmware-method)
         * hack done! (post_init.sh enable)
     * Add *vi /data/scripts/post_init.sh* *( from telnet )*
        ```
		killall -9 rtsp && rtsp >/dev/null 2>&1 &
		```
          or you can see rtsp user/pass (change every boot)

          from telnet command:
	  	```bash
	  	agetprop sys.camera_rtsp_url  # agetprop full (list all prop.)
	  	```
	  	![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/f4a401f3-f9f0-4fd3-a9f8-ea8605c8bba9)


	 	 rtsp://192.168.1.4:8554/360p (/720p /1080p /1296p)

	 	 rtsp://USER:PASS@192.168.1.4:8554/360p (/720p /1080p /1296p)

	 	 last ver. 4.3.4 change path:

		rtsp://192.168.1.4:8554/ch3

		"360p": "/ch3"
		"720p": "/ch2"
		"1296p":"/ch1"


    ```bash
    command_line:
      - sensor:
          name: aqara_rtsp_telnet
          command: "apk -q add inetutils-telnet && ( sleep 3; printf 'root\n'; sleep 1; printf 'clear\n'; sleep 1; printf 'agetprop sys.camera_rtsp_url\n'; sleep 1; ) | telnet 192.168.1.4 | sed '1,8d' | sed '$d'"
          value_template: "{{ value_json['720p'] }}"
          json_attributes:
            - 360p
            - 720p
            - 1080p
            - 1296p
     ```


---

* Sensor telnet command:
   * example "date"
 
```bash
command_line:
  - sensor:
      name: aqara_test
      command: "apk -q add inetutils-telnet && ( sleep 3; printf 'root\n'; sleep 1; printf 'clear\n'; sleep 1; printf 'date\n'; sleep 1; ) | telnet 192.168.1.4 | sed '1,8d' | sed '$d'"
      value_template: "{{ value }}"
```

 ![immagine](https://github.com/user-attachments/assets/1712abb3-1867-47ff-b352-063665389d68)

---

## Support me ##

**ko-fi.com** https://ko-fi.com/davide70304

---

## See also ##

[AqaraG3-armv7-binary](https://github.com/sdavides/AqaraG3-armv7-binary) AqaraG3 extra commands

[AqaraCameraHubfw](https://github.com/niceboygithub/AqaraCameraHubfw) Firmware 

[m3u8-HLS-Homeassistant](https://github.com/sdavides/m3u8-HLS-Homeassistant) Player m3u,mpd,mp4 playlist

[NginxReverse-Homeassistant](https://github.com/sdavides/NginxReverse-Homeassistant) ReverseProxy on HA

[go2rtc](https://github.com/AlexxIT/go2rtc) RTSP Proxy (HomeKit supported)
     
[WebRTC](https://github.com/AlexxIT/WebRTC) Card RTSP 

[EPGItaly-Homeassistant](https://github.com/sdavides/EPGItaly-Homeassistant)
