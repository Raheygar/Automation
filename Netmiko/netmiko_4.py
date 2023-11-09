from netmiko import ConnectHandler
router = {'host':'192.168.202.136','port':'22','username':'bh04308','password':'cisco','device_type':'cisco_ios','secret':'cisco','verbose':True}
ssh_client = ConnectHandler(**router)
prompt = ssh_client.find_prompt()      ##to check the prompt and print it 
print(prompt)
mode = ssh_client.check_enable_mode()  ##to check the 'enable' mode
print(mode)
if mode == False:                      ##if the mode is not enabled then enter loop
    ssh_client.enable()                ##get into enable mode
prompt = ssh_client.find_prompt()
print(prompt)
mode = ssh_client.check_config_mode()  ##to check if it is in the global configuration mode.
print(mode)
if mode == False:
    ssh_client.config_mode()
prompt = ssh_client.find_prompt()
print(prompt)
output = ssh_client.send_command('username rh04308 secret cisco')
ssh_client.exit_config_mode()      ## to exit the global configuration mode
print(output)
print(ssh_client.check_config_mode)
prompt = ssh_client.find_prompt()
print(prompt)
ssh_client.disconnect()
