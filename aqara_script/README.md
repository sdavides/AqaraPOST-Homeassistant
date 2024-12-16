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

## Requirement ##
telnet enable on G3 cam
