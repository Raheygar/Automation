from netmiko import ConnectHandler
def execute(device,command):
    ssh_client = ConnectHandler(**device)
    print("Enter enable mode ")
    ssh_client.enable()
    output = ssh_client.send_config_set(command)
    print(output)
    ssh_client.disconnect()
cmd = ['no router rip', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']
router = {'host':'192.168.202.136','port':22,'username':'bh04308','password':'cisco','secret':'cisco','device_type':'cisco_ios','verbose':True}
execute(device=router,command=cmd)