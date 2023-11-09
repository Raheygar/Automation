from netmiko import ConnectHandler
def execute(device,command):
    print(f"Connecting to {device['host']}")
    ssh_client = ConnectHandler(**device)
    print("Entering the enable mode ")
    output = ssh_client.send_command(command)
    print(output)
    print("Disconnecting from the device ")
    ssh_client.disconnect()
with open('devices.txt','r')as file:
    devices = file.read().splitlines()
with open('username.txt','r')as new_file:
    usernames = new_file.read().splitlines()
with open('password.txt','r')as conf_file:
    passwords = conf_file.read().splitlines()
try:
    for (ip,username,password) in zip(devices,usernames,passwords):
        router = {'host':ip,'port':22,'username':username,'password':password,'secret':'cisco','device_type':'cisco_ios','verbose':True}
        execute(device=router,command='show ip interface brief')
except Exception 