# AqaraPost_[Node-RED] HomeAssistant
  * Parallel container NodeRed with scripts AqaraPost-Homeassistant for integration Aqara G3 Camera.


## Requires
NodeRed-Companion *( install from HACS )*

MAC-ADDRESS Camera G3 *( lumi1.XXXXXX )*

Username/Password Aqara account
  * the values ​​in the "config" node will be generated from the username and password if valid


## Installation

Add custom component remote repository:

"https://github.com/sdavides/AqaraPOST-Homeassistant"


   ![immagine](https://github.com/user-attachments/assets/1f100850-d7db-40ca-a036-97254154b408)


## Settings

   ![immagine](https://github.com/user-attachments/assets/3d648c88-2b7d-4580-8e38-9d9ba3edfe7f)


## Update flow - Apply config

  * Delete file "flow.json"
    
    * ( usually into "/addon_configs/797fde71_nodered_aqara/" from SAMBA )

  * Update config

  * Restart addon

## Verify install

  * Verify values into "config" node
    
    ![immagine](https://github.com/user-attachments/assets/ab2c21f0-0a85-4398-9d29-bfe4e29df13c)


## Entity NodeCompanion ##
![immagine](https://github.com/user-attachments/assets/15e8632f-5c92-42f1-886b-96bec0633c43)
![immagine](https://github.com/user-attachments/assets/bb125094-8d71-403e-beff-2b323a461370)
