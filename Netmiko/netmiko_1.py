from netmiko import Netmiko
import getpass
password = getpass.getpass("Enter your secure password : ")
connection = Netmiko(host='192.168.202.136',port='22',username='bh04308',password=password,device_type='cisco_ios')
output = connection.send_command('show ip int brief')
print(output)
