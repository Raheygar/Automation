from netmiko import ConnectHandler
import getpass
password = getpass.getpass("Enter you password : ")
router = {'host':'192.168.202.136','port':22,'username':'bh04308','password':password,'secret':'cisco','device_type':'cisco_ios','verbose':True}
print(f"Connecting to {router['host']}")
ssh_client = ConnectHandler(**router)
print("Entering enable mode ")
ssh_client.enable()
command = ['username admin secret topsecret','exit']
output = ssh_client.send_config_set(command)
ssh_client.save_config()
print(output)
print(f"Closing the connection to {router['host']}")
ssh_client.disconnect()