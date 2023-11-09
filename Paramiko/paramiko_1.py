#Import the paramiko ssh client package for python
import paramiko
#Create a python object by invoking "paramiko.SSHClient()" method and declaring it as "ssh_client"
ssh_client = paramiko.SSHClient()
#Prints the type of Python object created.
print(type(ssh_client))
#Below statement is very important as the ssh connectivity will not work if it is not stated. It is necassaray
#because,when we shh to a box just before the login prompt we get a window for host key authentication we 
#have to manually click yes on it. The statement just adds the host key policy and ensures seamless 
#connectivity.
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#Call the "created pythonobject.connect(*kawrgs)" method and pass various arguments as suggested the important
#ones are listed below. The "look_for_keys" argument and "allow_agent" arguments are boolean and tells the
#connect function will not work if "keys" or "agents" are used to ssh the box as boolean values for those
#are 'FALSE'
#ssh_client.connect(hostname='192.168.202.136',port=22,username='bh04308',password='cisco',look_for_keys=False,allow_agent=False)
router = {'hostname':'192.168.202.136','port':'22','username':'bh04308','password':'cisco'}
print(f"Connecting to {router["hostname"]}")
ssh_client.connect(**router,look_for_keys=False,allow_agent=False)
#Below statement prints if the ssh connection is active or not.
print(ssh_client.get_transport().is_active())