# AqaraPost_[Node-RED] addon HomeAssistant

  AqaraPost_[Node-RED] - NodeRed mod for AqaraPost-Homeassistant.

  *Parallel container NodeRed with script AqaraPost-Homeassistant for integration Aqara G3 Camera.*

05/01/2025 🚨 Drop support for ARMv7 ([#2016](https://github.com/hassio-addons/addon-node-red/pull/2016))

## Requires
NodeRed-Companion *( install from HACS )*

Username/Password Aqara account

MAC address Camera G3 *( lumi1.XXXXXX )*


## Installation

Add custom component remote repository:

"https://github.com/sdavides/AqaraPOST-Homeassistant"


   ![immagine](https://github.com/user-attachments/assets/1f100850-d7db-40ca-a036-97254154b408)


## Setting

   ![immagine](https://github.com/user-attachments/assets/3d648c88-2b7d-4580-8e38-9d9ba3edfe7f)


## Update/Apply new config

  * Delete file "flow.json"
    
    * ( usually into "/addon_configs/797fde71_nodered_aqara/" from SAMBA )

  * Update config

  * Restart addon

## Verify install

  * Verify value into "config" node
    
    ![immagine](https://github.com/user-attachments/assets/ab2c21f0-0a85-4398-9d29-bfe4e29df13c)

    ![immagine](https://github.com/user-attachments/assets/c48aaefd-cd6c-45d9-b927-bd6129b839af)


