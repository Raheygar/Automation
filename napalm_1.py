from napalm import get_network_driver
import json
driver = get_network_driver('ios')
option_args = {'secret':'cisco'}
device = driver(hostname='192.168.202.136',username='bh04308',password='cisco',optional_args=option_args)
device.open()
output = device.get_facts()
dump = json.dumps(output,sort_keys=True,indent=4)
print(dump)
device.close()
