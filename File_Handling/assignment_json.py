#To work with http/https we have to import "requests" library and json library.
import requests
import json
#with "request.get(url)" method we get the response from the given url.
#json.loads() method converts/deserialize elemnets from the url into python objects.
response = requests.get('https://jsonplaceholder.typicode.com/todos')
py_obj = json.loads(response.text)
print(type(py_obj))
print(py_obj)
#We iterate over the converted python object(py_obj) and figure out the completed tasks in the object.
for tasks in py_obj:
    if tasks['completed'] == True:
        print(tasks)