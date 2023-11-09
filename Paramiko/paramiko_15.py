import paramiko_14
import getpass
password = getpass.getpass("Enter your secure password : ")
client = paramiko_14.get_connection('192.168.202.136','22','bh04308',password)
shell = paramiko_14.get_shell(ssh_client=client)
paramiko_14.sending_commands(shell,'terminal length 0')
paramiko_14.sending_commands(shell,'enable')
paramiko_14.sending_commands(shell,'cisco')
paramiko_14.sending_commands(shell,'show run')
output = paramiko_14.get_output(shell)
output_list = output.splitlines()
output_list =output_list[19:-1]
configuration = '\n'.join(output_list)
from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
backup = f"192.168.202.136-{year}-{month}-{day}"
with open(backup,'w')as file:
    file.write(configuration)