from netmiko import ConnectHandler
router = {'host':'192.168.202.136','port':'22','username':'bh04308','password':'cisco','secret':'cisco','device_type':'cisco_ios','verbose':True}
ssh_client = ConnectHandler(**router)
print("Entering enable mode")
ssh_client.enable()
# cmd = ['interface loopback 1','ip address 10.10.10.10 255.255.255.0','exit','username netmiko secret cisco']
cmd = """interface loopback 2
ip address 20.20.20.20 255.255.255.0
exit
username u3 secret cisco """
#ssh_client.send_config_set(cmd.split(';'))
ssh_client.send_config_set(cmd.split('\n'))
ssh_client.send_command('write memory')
prompt = ssh_client.find_prompt()
print(prompt)
print("Closing connection to the device")
ssh_client.disconnect()