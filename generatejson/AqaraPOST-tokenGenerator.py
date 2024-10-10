#!/usr/bin/env python3
import requests
import time
import uuid
import json
import urllib.parse
from Crypto.PublicKey import RSA
from Crypto.Hash import MD5
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64encode
from requests_toolbelt.utils import dump

import sys


print ('\n #### Token Generator AqaraPost ####')
print ('\n #### This is an automatic script to generate token for Node Red json HomeAssistant ####')
print (' #### for the Aqara Account, read on https://github.com/sdavides/AqaraPOST-Homeassistant ####')
print ('\n')
print ('#### Request info login: #### \n')

username = input("Enter your username: [example@example.com] \n")
password = input("Enter your password: [password] \n")
area = input("Enter your area: [EU],[CN],[RU],[USA],[KR],[OTHER]\n")


if username == '' :
        username = sys.argv[1]
if password == '' :
        password = sys.argv[2]
if area == '' :
        area = sys.argv[3]


class pyAqara():
    areas = {
        "CN": {
            "server": "https://aiot-rpc.aqara.cn",
            "appid": "444c476ef7135e53330f46e7",
            "appkey": "NULL"
        },
        "EU": {
            "server": "https://rpc-ger.aqara.com",
            "appid": "444c476ef7135e53330f46e7",
            "appkey": "NULL"
        },
        "RU":{
            "server": "https://rpc-ru.aqara.com",
            "appid": "444c476ef7135e53330f46e7",
            "appkey": "NULL"
        },
        "KR":{
            "server": "https://rpc-kr.aqara.com",
            "appid": "444c476ef7135e53330f46e7",
            "appkey": "NULL"
        },
        "USA": {
            "server" : "https://aiot-rpc-usa.aqara.com",
            "appid": "444c476ef7135e53330f46e7",
            "appkey": "NULL"
        },
        "OTHER": {
            "server" : "https://aiot-rpc-usa.aqara.com",
            "appid": "444c476ef7135e53330f46e7",
            "appkey": "NULL"
        }
    }


    pubkey = '''-----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCG46slB57013JJs4Vvj5cVyMpR
        9b+B2F+YJU6qhBEYbiEmIdWpFPpOuBikDs2FcPS19MiWq1IrmxJtkICGurqImRUt
        4lP688IWlEmqHfSxSRf2+aH0cH8VWZ2OaZn5DWSIHIPBF2kxM71q8stmoYiV0oZs
        rZzBHsMuBwA4LQdxBwIDAQAB
        -----END PUBLIC KEY-----'''


    def __init__(self, area="CN"):
        self.area = area
        self._userid = None
        self._token = None
        self._session = requests.session()
        self._session.headers.update({
            "User-Agent": "pyAqara/1.0.0",
            "App-Version": "3.0.0",
            "Sys-Type": "1", #0: iOS, 1: Android
            "Lang": "en",
            "Phone-Model": "pyAqara",
            "PhoneId": str(uuid.uuid4()).upper(),
        })


    @property
    def server(self):
        return self.areas[self.area]['server']


    @property
    def appid(self):
        return self.areas[self.area]['appid']


    @property
    def appkey(self):
        return self.areas[self.area]['appkey']


    @property
    def area(self):
        return self._area


    @area.setter
    def area(self, area):
        area = area.upper()
        if area not in self.areas.keys():
            area = "OTHER"
        self._area = area


    def encrypt_password(self, password):
        rsa = PKCS1_v1_5.new(RSA.importKey(self.pubkey))
        return b64encode(
            rsa.encrypt(MD5.new(password.encode()).hexdigest().encode())
        ).decode()


    def login(self, username, password):
        payload = {
                "account": username,
                "encryptType": 2,
                "password": self.encrypt_password(password)
        }
        req = self.request('POST', f'{self.server}/app/v1.0/lumi/user/login', json=payload)
        #DEBUG
        #print(dump.dump_all(req).decode("utf-8"))
        #print(json.dumps(req.json(), indent=4, sort_keys=True))
        print ('#### End Request #### \n')
        res = req.json()
        if res['code'] == 0:
            self._userid = res['result']['userId']
            self._token = res['result']['token']
            print ('\n #### Account info: #### \n')
            print ('\nToken:' + self._token )
							   
								
            print ('\nServer:' + (self.server).replace('https://','') )
            print ('\nAppID:' + self.appid )
							  
            print ('\nUserID:' + self._userid )
								
            return True
        return False


    def add_headers(self, payload):
        headers = {
            "Area": self.area,
            "Appid": self.appid,
            "Appkey": self.appkey,
            "Nonce": MD5.new(str(uuid.uuid4()).encode()).hexdigest(),
            "Time": str(round(time.time() * 1000)),
            "RequestBody": payload
        }
        if self._token is not None:
            headers['Token'] = self._token
        headers['Sign'] = self.sign_header(headers)
        del headers['Appkey']
        del headers['RequestBody']
        return headers


    def sign_header(self, headers):
        if headers.get('Token'):
            sign = 'Appid={Appid}&Nonce={Nonce}&Time={Time}&Token={Token}&{RequestBody}&{Appkey}'.format(**headers)
        else:
            sign = 'Appid={Appid}&Nonce={Nonce}&Time={Time}&{RequestBody}&{Appkey}'.format(**headers)
        return MD5.new(sign.encode()).hexdigest()


    def request(self, *args, **kwargs):
        method = args[0]
        if method == 'GET':
            payload = urllib.parse.urlencode(kwargs['params'])
        elif method == 'POST':
            if kwargs.get('json'):
                payload = json.dumps(kwargs['json'])
            elif kwargs.get('data'):
                payload = kwargs['data']
            elif kwargs.get('params'):
                payload = urllib.parse.urlencode(kwargs['params'])
        else:
            raise ValueError('Unsupported Method')
        kwargs.setdefault('headers', self.add_headers(payload))
        return self._session.request(*args, **kwargs)

aqara = pyAqara((area))

if aqara.login(username, password):
    print ('\n')

    print ('#### request post-login success ####')
    #params = {'firmwareVersion': '3.3.2', 'model': 'lumi.camera.gwpagl01'}
    #params = {'firmwareVersion': '0.0.0_0021', 'model': 'lumi.airrtc.agl001'}
    #params = {'firmwareVersion': '1.0.24', 'model': 'lumi.vibration.agl01'}

    # device query
    print ('\n #### device query ####')
    req = aqara.request('GET', f'{aqara.server}/app/v1.0/lumi/app/position/device/query', params='')
    print(json.dumps(req.json(), indent=4, sort_keys=True))
    #print(dump.dump_all(req).decode("utf-8"))

    print ('\n #### END script ####')
    print ('\n')
else:
    print('Login Failed!')
