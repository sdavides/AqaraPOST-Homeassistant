# AqaraPost_[Node-RED] addon HomeAssistant

  AqaraPost_[Node-RED] - NodeRed mod for AqaraPost-Homeassistant.

  *Parallel container NodeRed with script AqaraPost-Homeassistant for Aqara G3 Camera or FP2 Sensor.*

## Requires
NodeRed-Companion *( install from HACS )*

Username/Password Aqara account

MAC address device G3 camera/FP2 sensor *( lumi1-XXXXXX )*

server Aqara *[list aqara url](https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/generatejson/list_aqara_url.txt)*

## Installation

Add custom component remote repository:
"https://github.com/sdavides/AqaraPOST-Homeassistant"


   ![immagine](https://github.com/user-attachments/assets/1f100850-d7db-40ca-a036-97254154b408)


## Setting

   <img width="1097" height="649" alt="immagine" src="https://github.com/user-attachments/assets/69eeb4cb-aad2-4cc7-9de6-60ee5338131f" />



## Update/Apply new config

  * Delete "flows.json"
    
    * ( usually into "/addon_configs/797fde71_nodered_aqara/" from SAMBA )

  * Update config

  * Restart addon

## Verify install

  * Verify value into "config" node
    
    ![immagine](https://github.com/user-attachments/assets/ab2c21f0-0a85-4398-9d29-bfe4e29df13c)

    ![immagine](https://github.com/user-attachments/assets/c48aaefd-cd6c-45d9-b927-bd6129b839af)

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
