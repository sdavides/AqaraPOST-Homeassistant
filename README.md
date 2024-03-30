#  AqaraPOST-Homeassistant #

Goal: Replace Post request "Aqara Home" app on HomeAssistant

  * note: 
	* this flow is example and was developed for Aqara Hub G3 camera

## Requirement ##
* Your value from post request Aqara app:
  * appid  ( XXXXXXAPPIDXXXXXXXXXXX )
  * token ( XXXXXXTOKENXXXXXXXXXXX )
  * aqara url ( rpc-ger.aqara.com )
	* timezone ( it-IT ) -> es-ES/en-UK/de-DE/it-IT/pt-PT/es-ES
	* userid ( automatic, enter manual if not work )
	
## Method ##
* Method 1 NodeRed (recommended):
	* Import flow Aqara_G3_nodered.json 
	* Replace your value "config" node 
	* Deploy
		* note: you can use the script to generate your NoderRed json
		* [generatejson](https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/generatejson/README)
	
* Method 2 RestFul (without NodeRed):
	* Replace your value Aqara_G3_without_nodered.txt
	* Copy and paste Aqara_G3_without_nodered.txt on configuration.yaml
	* Restart HomeAssistant

 
## Find your Value ##
* Use BurpSuite or similar:
	* Follow [BurpSuite Guide](https://github.com/sdavides/AqaraPOST-Homeassistant/blob/main/Burp%20Suite%20Guide.pdf)
	* Download [AqaraAPP mod](https://drive.google.com/file/d/1Wfn_ynyCGvPwldjbbNGvZmYBKj5csuMy/view?usp=sharing)
 
## Why? ##
I have an Aqara Hub G3 camera on HomeAssistant but I can't control it, with the homekit connection I only have the alarm function.

## Install OK ##
![0](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/54a22cd1-fdf8-4dc3-b2d4-a0e03d269cb4)
![1](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/d6ebd1e4-707e-47f2-a473-ab88b3cc0126)
![2](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/104c9fda-c435-4929-9183-ef9f8456bf23)

