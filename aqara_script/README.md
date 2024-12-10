## Aqara G3 script ##
* Download folder "aqara_script" on "/config" :
  * change IP cam 192.168.x.x (telnet)
  * run shell command on HA
    
    result:

       /config/aqara_script/getprop_aqara.js
    
      * full properties

       /config/aqara_script/rtsp_aqara.js
    
       * rtsp url with password

configuration.yaml

    shell_command:
      recording_cam_aqara_on: /config/aqara_script/recording_cam_aqara_on.sh
      aqara_g3_telnet_json: /config/aqara_script/getprop_aqara.sh
      aqara_g3_rtsp_json: /config/aqara_script/rtsp_aqara.sh

## Requirement ##
telnet enable on G3 cam
