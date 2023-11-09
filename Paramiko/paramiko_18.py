import paramiko_16
import threading   ##Import the threading module
##Define a function where all the executeables for this process will be present and will be later called.
def backup_work(router):
    client = paramiko_16.gettting_connection(**router)
    shell = paramiko_16.get_shell(ssh_client=client)
    paramiko_16.sending_commands(shell,'terminal length 0')
    paramiko_16.sending_commands(shell,'enable')
    paramiko_16.sending_commands(shell,'cisco')
    paramiko_16.sending_commands(shell,'show run')
    output = paramiko_16.getting_output(shell)
    output_list = output.splitlines()
    output_list = output_list[18:-1]
    configuration = '\n'.join(output_list)
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    backup = f"{router['server_ip']}_{year}-{month}-{day}"
    with open(backup,'w')as file:
        file.write(configuration)
    paramiko_16.close_connection(ssh_client=client)
##Declare all the routers/devices as dictionaries
router1 = {'server_ip':'192.168.202.136','server_port':'22','user':'bh04308','passwd':'cisco'}
router2 = {'server_ip':'192.168.202.145','server_port':'22','user':'bh04308','passwd':'cisco'}
router3 = {'server_ip':'192.168.202.146','server_port':'22','user':'bh04308','passwd':'cisco'}
routers = [router1,router2,router3]
##Create an empty list called threads
threads = []
for router in routers:  ##Iterate over each element in the routers list
    ##Call the backup_work function and aplly as bellow 
    th = threading.Thread(target=backup_work,args=(router,))
    ##Whatever result is obtained from above call for individual list is stored in the "threads" list
    threads.append(th)
for th in threads:   ##Iterate over each thread in the now threads list containing elements.
    th.start()       ##start each thread
for th in threads:   ##Iterate over each thread in the threads list
    th.join()        ##Join all the started threads together.

