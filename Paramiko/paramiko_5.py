import myparamiko
linux = myparamiko.connect('192.168.202.147','22','raheygar','Shakun@004')
shell = myparamiko.get_shell(linux)
myparamiko.send_command(shell,'sudo su -')
myparamiko.send_command(shell,'Shakun@004')
myparamiko.send_command(shell,'users')
print(myparamiko.show_output(shell))