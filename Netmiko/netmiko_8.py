from netmiko import ConnectHandler
with open('devices.txt','r')as f1:
    devices = f1.read().splitlines()
with open('username.txt','r')as f2:
    usernames = f2.read().splitlines()
with open('password.txt','r')as f3:
    password = f3.read().splitlines()
devices_list = list()
for ip in devices:
    router = {'host':ip,'port':22,'username':'','password':'','secret':'cisco','device_type':'cisco_ios','verbose':True}
#print(devices_list)
    for user in usernames:
        router = {'host':ip,'port':22,'username':user,'password':'','secret':'cisco','device_type':'cisco_ios','verbose':True}
        devices_list.append(router)
        print(devices_list)



    




            