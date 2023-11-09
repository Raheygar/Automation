import requests
import json
#Defining the endpoints:
api_endpoint = "https://192.168.202.150:443/web_api/"
username = 'admin'
password = 'admin123'
#Define parameters about what you want to do. For example a rule :
rule = {
    'name':'Testing rule',
    'source':'20.20.20.20',
    'destination':'10.10.10.10',
    'service':80,
    'action':'drop'
    }
#Convert the rule to json
data = json.dumps(rule)
#Authenticate to the firewall:
session = requests.session()
session.auth = (username,password)
#Send the api the rule to update:
response = session.post(f"{api_endpoint}/add-rule",data=data)
#Check the response status code
if response.status_code != 200:
    print(f"Error adding firewall rule:{response.text}")
else:
    print("Firewall rule added successfully")