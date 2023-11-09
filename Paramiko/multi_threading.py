import paramiko_9
import threading
def backup(router):
    client = paramiko_9.connect(**router)
    shell = paramiko_9.get_shell(ssh_client=client)
    paramiko_9.send_command(shell,'terminal length 0')
    paramiko_9.send_command(shell,'enable')
    paramiko_9.send_command(shell,'cisco')
    paramiko_9.send_command(shell,'show run')
    output = paramiko_9.show(shell)
    output_list = output.splitlines()
    output_list = output_list[18:-1]
    configuration = '\n'.join(output_list)
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    file_name = f"{router['server_ip']}_{day}-{month}-{year}"
    with open(file_name,'w')as f:
        f.write(configuration)
router1 = {'server_ip':'192.168.202.136','server_port':'22','user':'bh04308','passwd':'cisco'}
router2 = {'server_ip':'192.168.202.145','server_port':'22','user':'bh04308','passwd':'cisco'}
router3 = {'server_ip':'192.168.202.146','server_port':'22','user':'bh04308','passwd':'cisco'}
routers = [router1,router2,router3]
threads = list()   ##creating an empty threads list and it will be filled with each working thread as element.
for router in routers:
    th =threading.Thread(target=backup,args=(router,))
    threads.append(th)
for th in threads:  ##starting each thread in the threads list.
    th.start()
for th in threads:  ##joining each thread with the next after each thread completeion.
    th.join()
   
    
    