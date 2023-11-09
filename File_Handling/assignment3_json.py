import requests
import json
import csv
response = requests.get('https://jsonplaceholder.typicode.com/users')
py_obj = json.loads(response.text)
print(type(py_obj))
# print(py_obj)
with open('details.csv','w',newline = '')as f:
    writer = csv.writer(f)
    writer.writerow(['name','city','lat','long','company'])
    for data in py_obj:
        name_1 = data['name']
        city   = data['address']['city']
        lat    = data['address']['geo']['lat']
        long   = data['address']['geo']['lng']
        company = data['company']['name']
        csv_data = (name_1,city,lat,long,company)
        writer.writerow(csv_data)