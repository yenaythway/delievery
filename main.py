import socket
import threading
import datetime
host = '127.0.0.1'
port = 55555
sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.bind((host, port))
sever.listen()

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)

        except:
            pass

def receive():
    while True:
        client, address = sever.accept()
        connect_time = datetime.datetime.now()
        client.send('NICK'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        print(f'"{name}" connected with "{str(address)}" at "{connect_time}"')

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('Sever is listening')
receive()
