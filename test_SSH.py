import paramiko 

# create an SSH client object
ssh = paramiko.SSHClient()

# automatically add the server's host key
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to the server
ssh.connect(hostname='pi2', username='pi2', password='raspberry')

# execute a command on the server
stdin, stdout, stderr = ssh.exec_command('ls')

# print the output of the command
print(stdin.read().decode())

# close the connection
ssh.close()
