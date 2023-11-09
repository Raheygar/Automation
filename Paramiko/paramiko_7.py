import paramiko_6
import time
client = paramiko_6.connect('192.168.202.136','22','bh04308','cisco')
shell = paramiko_6.get_shell(client)
paramiko_6.send_command(shell,'terminal length 0')
paramiko_6.send_command(shell,'enable')
paramiko_6.send_command(shell,'cisco')
paramiko_6.send_command(shell,'show run')
output = paramiko_6.get_output(shell)
config_list = output.splitlines()
config_list = config_list[18:-1]
output = '\n'.join(config_list)
from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
file_backup = f"Backup_Data {year}_{month}_{day}.txt"
print(file_backup)
with open(file_backup,'w')as f:
    f.write(output)
paramiko_6.close_connection(ssh_client=client)
