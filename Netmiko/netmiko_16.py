from netmiko import ConnectHandler
import getpass
password = getpass.getpass("Enter your password : ")
router = {'host':'192.168.202.136','port':22,'username':'bh04308','password':'cisco','secret':'cisco','device_type':'cisco_ios','verbose':True}
print(f"Connecting to {router['host']}")
ssh_client = ConnectHandler(**router)
print("Entering enabling mode ")
ssh_client.enable()
commands = ['access-list 101 permit tcp any any eq 80','access-list 101 permit tcp any any eq 443','access-list 101 deny ip any any','exit']
output = ssh_client.send_config_set(commands)
print(output)
print(f"Closing connection to {router['host']}")
ssh_client.disconnect()
