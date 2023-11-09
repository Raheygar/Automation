from netmiko import ConnectHandler
with open('devices.txt','r')as f:
    devices = f.read().splitlines()
device_list = list()
for ip in devices:
        router = {
        'device_type':'cisco_ios',
        'host':ip,
        'port':'22',
        'username': 'bh04308',
        'password':'cisco',
        'secret':'cisco',
        'verbose':True
        }
        device_list.append(router)
for device in device_list:
    print("Connecting to the device")
    ssh_client = ConnectHandler(**device)
    print("Enabling the 'enable' mode")
    ssh_client.enable()
    file = input(f'Please enter the configuration file for {device["host"]}')
    ssh_client.send_config_from_file(file)
    ssh_client.disconnect()

    

    