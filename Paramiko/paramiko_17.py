import paramiko_16       ##Importing module created by me "paramkio_16"
##Declaring the device details as a dictionary
router1 ={'server_ip':'192.168.202.136','server_port':'22','user':'bh04308','passwd':'cisco'}
##Calling the "getting_connection" method and storing it in client variable
client = paramiko_16.gettting_connection(**router1)
##Calling the "get_shell" method from paramiko_16 to enter shell of the device
shell = paramiko_16.get_shell(ssh_client=client)
##Calling the "sending_commands" method form the paramiko_16 module to send commands to teh device
paramiko_16.sending_commands(shell,'terminal length 0')
paramiko_16.sending_commands(shell,'enable')
paramiko_16.sending_commands(shell,'cisco')
paramiko_16.sending_commands(shell,'show run')
##Calling the "getting_output" method to extarct the output
output = paramiko_16.getting_output(shell)
##Convert the output into a list and initialize to "output_list"
output_list = output.splitlines()
##Slice the above list using indexing and store it in "output-list" from where you need the data
output_list = output_list[18:-1]
##Join the above elements stored in "output_list" using ".join()" and store it in "confgiuration"
configuration = '\n'.join(output_list)
##Import "datetime" to record the date and time currently.
from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
Backup = f"{router1['server_ip']}-{year}-{month}-{day}"
##Create a file and write the contents of "configuration" into the file.
with open(Backup,'w')as file:
    file.write(configuration)
##Closing the connection.
paramiko_16.close_connection(ssh_client=client)