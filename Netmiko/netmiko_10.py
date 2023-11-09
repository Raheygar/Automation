from netmiko import ConnectHandler
import threading
with open('devices.txt','r')as new:
    devices = new.read().splitlines()
def backup_configuration(device):
    router = {'host':device,'port':22,'username':'bh04308','password':'cisco','secret':'cisco','verbose':True,'device_type':'cisco_ios'}
    print("Connecting to the device")
    ssh_client = ConnectHandler(**router)
    print("Entering the enable mode")
    ssh_client.enable()
    print("Extarcting backup of the device")
    output = ssh_client.send_command("show run")
    prompt = ssh_client.find_prompt()
    hostname = prompt[0:-1]
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    file = f'{hostname}_{year}-{month}-{day}.txt'
    with open(file,'w')as backup:
        backup.write(output)
        print("The backup of the device was extracted successfully")
        print("#"*30)
threads = []
for device in devices:
    th = threading.Thread(target=backup_configuration,args=(device,))
    threads.append(th)
for th in threads:
    th.start()
for th in threads:
    th.join()

