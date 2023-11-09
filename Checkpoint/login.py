import json
import requests
#Declare parameters to interact with the checkpoint firewall api's
ip = '192.168.202.150'
username = 'admin'
password = 'admin123'
#Declare endpoint
url = "https://192.168.202.150/web_api/"
payload = {'user':username,'password':password}
#Send login requests to the firewall REST API
response = requests.post(f"{url}/login",json=payload,verify=False,timeout=5)
#Get the session-id
if response.status_code != 200:
    print("Session Established!!")
else:
    print("Cannot login to the dvice")
#Get rule details from the firewall api
rule_response = requests.get(f"{url}/show-access-rulebase",timeout=5,verify=False)
# print(rule_response.content)
with open('rule_reponse.html','wb')as file:
    file.write(rule_response.content)
if rule_response.status_code == 200:
    print("Rules accessed!!")
    print(rule_response.status_code)
else:
    print("Cannot pull rules from firewalls!!")
#Logging out from firewalls:
logout = requests.post(f"{url}/logout",timeout=5,verify=False)
if logout.status_code == 200:
    print("logout successfull")
#Set session token in headers for future requests
# headers = {"x-chkp=sid":session_token}