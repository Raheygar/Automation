import paramiko_8
router1 = {'server_ip':'192.168.202.136','server_port':'22','user':'bh04308','passwd':'cisco'}
router2 = {'server_ip':'192.168.202.145','server_port':'22','user':'bh04308','passwd':'cisco'}
router3 = {'server_ip':'192.168.202.146','server_port':'22','user':'bh04308','passwd':'cisco'}
routers = [router1,router2,router3]
for router in routers: 
    client = paramiko_8.connect(**router)
    shell = paramiko_8.get_shell(ssh_client=client)
    paramiko_8.send_command(shell,'terminal length 0')
    paramiko_8.send_command(shell,'enable')
    paramiko_8.send_command(shell,'cisco')
    paramiko_8.send_command(shell,'show run')
    output = paramiko_8.output(shell)
    output_list = output.splitlines()
    output_list = output_list[18:-1]
    configuration = '\n'.join(output_list)
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    file_name = f"{router['server_ip']}_{year}-{month}-{day}"
    with open(file_name,'w')as f:
        f.write(configuration)