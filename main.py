import socket
import threading
import datetime
import database
host = '127.0.0.1'
port = 55551
sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.bind((host, port))
sever.listen()
database=database.DataBase()
# def handle(client):
#     while True:
#         try:
#             message = client.recv(1024).decode('ascii')
#             print(message)
#             if message.startswith('Private Chat'):
#                 obj_name = message.split('(')[1].split(')')[0]
#                 message = message.split('): ')[1]
#                 sub_name = names[clients.index(client)]
#                 client_obj = clients[names.index(obj_name)]
#                 client_obj.send(f"{sub_name}:{message}".encode('ascii'))
#                 client.send(f"{sub_name} : {message}".encode('ascii'))
#
#             elif message.startswith('Group Chat'):
#
#                 clients_name=message.split('/')[1].split(',')
#
#                 message=message.split('/')[2]
#
#                 sub_name = names[clients.index(client)]
#
#                 client.send(f"{sub_name} : {message}".encode('ascii'))
#                 for name in clients_name:
#                     clients[names.index(name)].send(f"{sub_name} : {message}".encode('ascii'))
#
#             else:
#                 client.send("Invalid message format.".encode('ascii'))
#
#         except:
#             index = clients.index(client)
#             clients.remove(client)
#             client.close()
#             name = names[index]
#             broadcast(f'{name} left the chat'.encode('ascii'))
#             names.remove(name)
#             break


def receive():
    while True:
        client, address = sever.accept()
        # connect_time = datetime.datetime.now()
        print(' connected')

        avilable_food=database.req_food()
        print(avilable_food)
        client.send(avilable_food.encode('ascii'))
        ordered_food=client.recv(1024).decode('ascii')
        shop_price=database.find_shop(ordered_food)
        client.send(shop_price.encode('ascii'))
        # # name = client.recv(1024).decode('ascii')
        #
        # thread = threading.Thread(target=handle, args=(client,))
        # thread.start()

print('Sever is listening')
receive()
#history
