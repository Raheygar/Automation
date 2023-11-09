from netmiko import ConnectHandler
import threading
with open('devices.txt','r')as file:
    routers = file.read().splitlines()
def interface_status(ip):
    router = {'host':ip,'port':22,'username':'bh04308','password':'cisco','secret':'cisco','device_type':'cisco_ios','verbose':True}
    print(f"Connecting to {router['host']}")
    ssh_client = ConnectHandler(**router)
    print("Enabling the enable mode")
    ssh_client.enable()
    interface = input("Enter the interface you wish to enable or disable ")
    output = ssh_client.send_command("show interface " + interface)
    if 'Invalid input detected' in output:
        print("Wrong interface entered ")
    else:
        first_line = output.splitlines()[0]
        print(first_line)
        if not 'ip' in first_line:
            print("The interface is down. Enabling the interface ")
            commands = ['interface ' + interface,'no shutdown','exit']
            output = ssh_client.send_config_set(commands)
            print(output)
            ssh_client.save_config()
        else:
            print("The interface is up.")
    print(f"Closing the connection to {router['host']}")
    ssh_client.disconnect()
threads = []
for ip in routers:
    th = threading.Thread(target=interface_status,args=(ip,))
    threads.append(th)
for th in threads:
    th.start()
for th in threads:
    th.join()
