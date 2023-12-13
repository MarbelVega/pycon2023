import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Añade automáticamente la clave del host si no está en known_hosts
ssh_client.connect('nombre_del_servidor', username='tu_usuario', password='tu_contraseña')

stdin, stdout, stderr = ssh_client.exec_command('tu_comando')
print(stdout.read().decode())  # Imprime la salida del comando ejecutado

ssh_client.close()  # Cierra la conexión