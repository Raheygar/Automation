import paramiko
import time
def connect(server_ip,port_nu,user,passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("Connecting to the device")
    ssh_client.connect(hostname=server_ip,port=port_nu,username=user,password=passwd,allow_agent=False,look_for_keys=False)
    print(ssh_client.get_transport().is_active())
    return ssh_client
def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell
def send_command(shell,command,timeout=10):
    shell.send(command + '\n')
    time.sleep(timeout)
def get_output(shell,n=10000):
    output = shell.recv(n)
    return output.decode()
def close_connection(ssh_client):
    if ssh_client.get_transport().is_active == True:
        print("Closing connection to the device")
        ssh_client.close()
# if __name__ == '__main__'
# client = connect('192.168.202.136','22','bh04308','cisco')
# shell = get_shell(client)
# send_command(shell,'terminal length 0')
# send_command(shell,'show version')
# print(get_output(shell))