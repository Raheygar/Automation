import paramiko
import time
def get_connection(server_ip,server_port,user,passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Connecting to the device")
    ssh_client.connect(hostname=server_ip,port=server_port,username=user,password=passwd,allow_agent=False,look_for_keys=False)
    print(ssh_client.get_transport().is_active())
    return ssh_client
def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell
def sending_commands(shell,command,timeout=10):
    shell.send(command+'\n')
    time.sleep(timeout)
def get_output(shell,n=10000):
    output = shell.recv(n)
    return output.decode()
def close_connection(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print("Closing connection to the device")
        ssh_client.close()
