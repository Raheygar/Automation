from netmiko import ConnectHandler
firewall = {'host':'192.168.202.136','port':22,'username':'bh04308','password':'cisco','device_type':'cisco','verbose':True}
ssh_client = ConnectHandler(**firewall)
ssh_client.se