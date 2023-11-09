import psutil
##Get interfaces of the system
interfaces = psutil.net_if_addrs()
for interface in interfaces.items():
    print(interface)