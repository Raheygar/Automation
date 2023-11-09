from netmiko import ConnectHandler
import threading
with open('devices.txt','r')as file:
    devices = file.read().splitlines()
with open('username.txt','r')as f:
    usernames = f.read().splitlines()
with open('password.txt','r')as k:
    passwords = k.read().splitlines()
def arp_details(ip):
    router = {'host':ip,'port':22,'username':username,'password':password,'secret':'cisco','device_type':'cisco_ios','verbose':True}
    print(f"Connecting to {router['host']}")
    ssh_client = ConnectHandler(**router)
    print("Entering the enable mode ")
    ssh_client.enable()
    output = ssh_client.send_command("show arp")
    print(output)
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    arp_file = f"{router['host']}_{year}-{month}-{day}.txt"
    with open(arp_file,'w')as new:
        new.write(output)
    print(f"Closing connection to {router['host']}")
    ssh_client.disconnect()
threads = []
for (ip,username,password) in zip(devices,usernames,passwords):
    th = threading.Thread(target=arp_details,args=(ip,))
    threads.append(th)
for th in threads:
    th.start()
for th in threads:
    th.join()

