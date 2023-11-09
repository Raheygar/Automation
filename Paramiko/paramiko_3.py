import paramiko
import time
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router1 = {'hostname':'192.168.202.136','port':'22','username':'bh04308','password':'cisco'}
router2 = {'hostname':'192.168.202.145','port':'22','username':'bh04308','password':'cisco'}
router3 = {'hostname':'192.168.202.146','port':'22','username':'bh04308','password':'cisco'}
routers = [router1,router2,router3]
for router in routers:
    print(f"Connecting to {router['hostname']}")
    ssh_client.connect(**router,allow_agent=False,look_for_keys=False)
    print(ssh_client.get_transport().is_active())
    shell = ssh_client.invoke_shell()
    shell.send('terminal length 0\n')
    shell.send('enable\n')
    shell.send('cisco\n')
    shell.send('configure terminal\n')
    shell.send('router ospf 1\n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('write memory\n')
    time.sleep(5)
    output = shell.recv(10000).decode('utf-8')
    print(output)
    if ssh_client.get_transport().is_active() == True:
        print(f"Closing connection to {router['hostname']}")
        ssh_client.close()