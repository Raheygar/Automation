from netmiko import ConnectHandler
with open('all_info.txt','r')as read_file:
    list_1 = read_file.read().splitlines()
    print(list_1)
devices = []
for item in list_1:
    tmp = item.split(':')
    devices.append(tmp)
print(devices)
for device in devices:
    router = {'host':device[1],'port':22,'username':device[2],'password':device[3],'secret':'cisco','device_type':device[0],'verbose':True}
    print(f"Connecting to {device[1]}")
    ssh_client = ConnectHandler(**router)
    print("Entering enable mode")
    ssh_client.enable()
    conf_file = input(f"Please enter a configuration file for {device[1]} ")
    with open(conf_file,'r')as configu:
        send_conf = configu.read().splitlines()
    output = ssh_client.send_config_set(send_conf)
    print(output)
    full_config = ssh_client.send_command_timing("show run")
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    export_data = f"{device[1]}_{year}-{month}-{day}.txt"
    with open(export_data,'w')as new_data:
        new_data.write(full_config)
    print(f"Disconnecting from {device[1]}")
    ssh_client.disconnect()
