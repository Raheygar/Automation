import paramiko
import time
import getpass
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password = getpass.getpass('Enter password :')
linux = {'hostname':'192.168.202.147','port':'22','username':'raheygar','password':password}
print(f"Connecting to {linux['hostname']}")
ssh_client.connect(**linux,allow_agent=False,look_for_keys=False)
print(ssh_client.get_transport().is_active())
shell = ssh_client.invoke_shell()
shell.send('sudo su -\n')
shell.send('Shakun@004\n')        ###This is the sudo password to start access in 'root' mode. 
time.sleep(5)
output = shell.recv(10000).decode('utf-8')
print(output)
if ssh_client.get_transport().is_active():
    print(f"Closing connection to {linux['hostname']}")
    ssh_client.close()