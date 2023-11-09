from netmiko import ConnectHandler
import time,schedule,getpass
username = input("Enter your username : ")
password = getpass.getpass("Enter your password : ")
firewall = {'host':'192.168.202.136','port':22,'username':username,'password':password,'device_type':'checkpoint_gaia','verbose':True}
print(f"Connecting to the firewall{firewall['host']}")
ssh_client = ConnectHandler(**firewall)
tcp_dump = "tcpdump -i eth0 'src host ip and dst host ip'"
ssh_client.send_command_timing(tcp_dump)
time.sleep(10)
ssh_client.write_channel('\x03')
output = ssh_client.read_until_prompt()
print(output)
##Disconnecting from the firewall
print(f"Disconnecting from the firewall{firewall['host']}")
ssh_client.disconnect()