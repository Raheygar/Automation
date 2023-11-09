from netmiko import ConnectHandler
import getpass
password = getpass.getpass("Enter your secure password")
router = {'host':'192.168.202.136','port':'22','username':'bh04308','secret':'cisco','password':'cisco','device_type':'cisco_ios','verbose':True}
print("Connecting to the device")
ssh_client = ConnectHandler(**router)
print("Entering the enable mode")
ssh_client.enable()                           ## Enter into the enable mode.
print("Sending connection from a file")
ssh_client.send_config_from_file('ospf.txt')  ## Used to get the info from a file in the same directory.
print("Closing connection to the device")
ssh_client.disconnect()
