import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect('192.168.0.2', port=22, username='pi', password='raspberry')

stdin, stdout, stderr = ssh.exec_command("ls -al")
output = stdout.readlines()

print(type(output))
print("\n".join(output));

ssh.close()