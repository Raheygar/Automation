from netmiko import ConnectHandler  ##from netmiko module import class 'ConnectHandler'
import getpass                      ##import 'getpass' module to secure password
##Get password as input
password = getpass.getpass("Enter your secure password : ")
##Declare a dictionary with the device details
router = {'host':'192.168.202.136','port':22,'username':'bh04308','password':password,'secret':'cisco','verbose':True,'device_type':'cisco_ios'}
##Call 'ConnectHandler' function for ssh connectivity
connection = ConnectHandler(**router)
output = connection.send_command('show ip interface brief')
print(output)
print("Closing connection to the device")
connection.disconnect()   ##Closing the connection to the device 