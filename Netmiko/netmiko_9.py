from netmiko import ConnectHandler
with open('devices.txt','r')as new:
    devices = new.read().splitlines()
for ip in devices:
    router = {'host':ip,'port':22,'username':'bh04308','password':'cisco','secret':'cisco','device_type':'cisco_ios','verbose':True}
    print("Connecting to the device")
    ssh_client = ConnectHandler(**router)
    print("Entering the enable mode")
    ssh_client.enable()
    output = ssh_client.send_command("show run")
    prompt = ssh_client.find_prompt()
    hostname = prompt[0:-1]
    print(hostname)
    backup_file = f'{hostname}.txt'
    with open(backup_file,'w')as f:
        f.write(output)
        print("The backup is completed successfully")
        print("#"*30)

