import paramiko
import time
def connect(server_ip,server_port,user,passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Connecting to {server_ip}")
    ssh_client.connect(hostname=server_ip,port=server_port,username=user,password=passwd,allow_agent=False,look_for_keys=False)
    print(ssh_client.get_transport().is_active())
    return ssh_client
def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell
def send_command(shell,command,timeout=2):
    shell.send(command + '\n')
    time.sleep(timeout)
def show_output(shell,n=10000):
    output = shell.recv(n)
    return output.decode('utf-8')
def closed(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print("Closing connection")
        ssh_client.close()
if __name__ == '__main__':
    router = {'server_ip':'192.168.202.136','server_port':'22','user':'bh04308','passwd':'cisco'}
    client = connect(**router)
    shell = get_shell(client)
    send_command(shell,'terminal length 0')
    send_command(shell,'show version')
    print(show_output(shell))
        
