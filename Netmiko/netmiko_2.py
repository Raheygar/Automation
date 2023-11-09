from netmiko import Netmiko  ##import the Netmiko class from netmiko module
import getpass               ##import the getpass module to secure the password entered
##import 'threading' module to start process for each device independently and simultaneously and then joining
##them together so that the execution is faster.
import threading 
##ask for password input form the user and store it securely            
password = getpass.getpass("Enter your secure password : ") 
##Enter the device details and initialize them into dictionaries for later use.
router1 = {'host':'192.168.202.136','port':'22','username':'bh04308','password':password,'device_type':'cisco_ios'}
router2 = {'host':'192.168.202.145','port':'22','username':'bh04308','password':password,'device_type':'cisco_ios'}
router3 = {'host':'192.168.202.146','port':'22','username':'bh04308','password':password,'device_type':'cisco_ios'}
#Create a list 'routers' and enter the dictionaries created earlier as elemnets.
routers = [router1,router2,router3]
#Initialize an empty list called threads
threads = []
##Declare a function for connecting to device and getting output of the device.
def backup(router):
    print(f"Connecting to {router['host']} : ")
    connetion = Netmiko(**router)
    output = connetion.send_command('show ip interface brief')
    #Create a list for the output above.
    output_lines = output.splitlines()
    output_lines =output_lines[1:]
    output_conf = '\n'.join(output_lines)  #join the elements after extracting data from the list.
    #import datetime for getting date and time details
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    file_name = f"{router['host']}-{day}-{month}-{year}"
    #create a new file where the extracted configuration of the device will be written.
    with open (file_name,'w')as f:
        f.write(output_conf)
for router in routers:  ##Iterate over the devices.
    ##import function 'Thread' from threading module. It takes two arguments target which takes in the
    ##name of the function without the parenthesis'()' and the 'args' take in the argunent of the declared
    ##function as tuple and that is why comma is necassary.
    th = threading.Thread(target=backup,args=(router,))
    ##upload above results into the empty list created 'threads'
    threads.append(th)
for th in threads:  ##Iterate over the list 'threads' to start each 'thread' 
    th.start()      ##call the 'start()' function to start each process in the threads.
for th in threads:  ##Iterate over the list 'threads'  
    th.join()       ##Call the function 'join' to join each thread after completion.
