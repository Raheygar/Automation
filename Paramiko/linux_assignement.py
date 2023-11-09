import paramiko_10
import getpass
username = input("Enter your username : ")
password = getpass.getpass("Enter your secure password")
client = paramiko_10.connect('192.168.202.147','22',username,passwd=password)
shell = paramiko_10.get_shell(ssh_client=client)
new_user = input("Enter the user you want to create : ")
command = 'sudo useradd -m -d /home/' +new_user+ ' -s /bin/bash ' +new_user
paramiko_10.send_command(shell,command)
paramiko_10.send_command(shell,password)
decision = input("Do you want to display the user created ? | y/n : ")
if decision == 'y':
    paramiko_10.send_command(shell,'cat /etc/passwd')
    output = paramiko_10.show_output(shell)
    print(output)