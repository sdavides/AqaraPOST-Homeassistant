# AqaraPost_[Node-RED] addon HomeAssistant

  AqaraPost_[Node-RED] - NodeRed mod for AqaraPost-Homeassistant.

  *Parallel container NodeRed with script AqaraPost-Homeassistant for Aqara G3 Camera or FP2 Sensor.*

## Requires
NodeRed-Companion *( install from HACS )*

Username/Password Aqara account

G3 camera/FP2 sensor MAC Address [ lumi1.*1a2b3c4d5c* ]

server Aqara *[list aqara url](https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/generatejson/list_aqara_url.txt)*

## Installation

Add custom component remote repository:
"https://github.com/sdavides/AqaraPOST-Homeassistant"


   <img width="852" height="446" alt="immagine" src="https://github.com/user-attachments/assets/a75d5dff-c3a1-4253-9340-f5936e0aaecd" />



## Setting

<img width="872" height="588" alt="immagine" src="https://github.com/user-attachments/assets/2de84ed5-0a72-4658-9075-ee80fa137f9d" />




## Update/Apply new config

  * Delete "flows.json"
    
    * ( usually into "/addon_configs/XXX_nodered_aqara/" from SAMBA )

  * Update config

  * Restart addon

## Verify install

  * Check the value in the "config" node
    
    <img width="809" height="468" alt="immagine" src="https://github.com/user-attachments/assets/413bcbe6-668e-4379-9810-d814235c1f1c" />


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
