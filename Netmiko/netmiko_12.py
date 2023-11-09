from netmiko import ConnectHandler
import threading
with open('devices.txt','r')as file:
    devices = file.read().splitlines()
with open('username.txt','r')as fi:
    usernames = fi.read().splitlines()
with open('password.txt','r')as fil:
    passwords = fil.read().splitlines()
dev_list = []
for (ip,username,password) in zip(devices,usernames,passwords):
    firewall = {'host':ip,'port':22,'username':username,'password':password,'secret':'cisco','device_type':'cisco_ios','verbose':True}
    dev_list.append(firewall)
    print("Connecting to {firewall['host']}")
    ssh_client = ConnectHandler(**firewall)
    output = ssh_client.send_command("show run")
    print(output)
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    backup = f"{firewall['host']}_{year}-{month}-{day}.txt"
    with open(backup,'w')as f:
        f.write(output)
        print("Configuratuion of the device has been backed successfully")
    print("Disconnecting the device")
    ssh_client.disconnect()