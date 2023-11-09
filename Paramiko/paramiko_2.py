import paramiko
import time
import getpass
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password = getpass.getpass('Enter password :')
router = {'hostname':'192.168.202.136','port':'22','username':'bh04308','password':password}
print(f"Connecting to {router['hostname']}")
ssh_client.connect(**router,allow_agent=False,look_for_keys=False)
print(ssh_client.get_transport().is_active())
shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('enable\n')
shell.send('cisco\n')
shell.send('configure terminal\n')
shell.send('do show ip int bri\n')
time.sleep(1)
output = shell.recv(10000)
print(type(output))
output = output.decode('utf-8')
print(output )
if ssh_client.get_transport().is_active() == True:
    print(f"Closing connection to {router['hostname']}")
    ssh_client.close()