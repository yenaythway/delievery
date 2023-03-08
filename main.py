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
#         except Exception as error:
#             print(error)


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
        # name = client.recv(1024).decode('ascii')
        #
        # thread = threading.Thread(target=handle, args=(client,))
        # thread.start()

print('Sever is listening')
receive()
#history