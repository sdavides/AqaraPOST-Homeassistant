#### Generate token from username and password ####

thank you [Wh1terat](https://gist.github.com/Wh1terat/c4a4c665d692af461796e5eee9f5461d)

#### command for generate token: ####
  * requirement: 
	* python3
         * pycryptodome *( pip3 install pycryptodome )*

```bash
wget -q https://raw.githubusercontent.com/sdavides/AqaraPOST-Homeassistant/main/generatejson/AqaraPOST-tokenGenerator.py --output-document=/tmp/AqaraPOST-tokenGenerator.py && chmod +x /tmp/AqaraPOST-tokenGenerator.py && /tmp/AqaraPOST-tokenGenerator.py
```
![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/f6ca48c6-1c5a-4557-b9db-3c9fab0d707b)

-------

#### Generate flow json with your values ####

#### command for first device: ####
```bash
wget -q https://raw.githubusercontent.com/sdavides/AqaraPOST-Homeassistant/main/generatejson/AqaraPOST-Homeassistant.sh --output-document=/tmp/AqaraPOST-Homeassistant.sh && chmod +x /tmp/AqaraPOST-Homeassistant.sh && /tmp/AqaraPOST-Homeassistant.sh
```

#### command for second device: (entity end "_2") ####
```bash
wget -q https://raw.githubusercontent.com/sdavides/AqaraPOST-Homeassistant/main/generatejson/AqaraPOST-Homeassistant_2device.sh --output-document=/tmp/AqaraPOST-Homeassistant.sh && chmod +x /tmp/AqaraPOST-Homeassistant.sh && /tmp/AqaraPOST-Homeassistant.sh
```

![immagine](https://github.com/sdavides/AqaraPOST-Homeassistant/assets/31100253/e4acedf1-f19d-4db6-a03c-fc2ab5ad655c)

