import paramiko_11
import getpass
import threading
password = getpass.getpass('Enter your secure password : ')
client = paramiko_11.get_connect('192.168.202.136','22','bh04308',password)
shell = paramiko_11.get_shell(client)
paramiko_11.sending_commands(shell,'terminal length 0')
paramiko_11.sending_commands(shell,'show users')
output = paramiko_11.get_output(shell=shell)
with open('users.txt','w')as file:
    file.write(output)