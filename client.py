import socket
import threading
import userservice
user = userservice.UserService()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55551))
def receive():

    while True:
        try:
            avilable_food = client.recv(1024).decode('ascii').split(',')
            if avilable_food != None:
                ordered_food=user.chose_food(avilable_food)
                client.send(ordered_food.encode('ascii'))
                shop_price=client.recv(1024).decode('ascii')
                shop_price = shop_price.split(',')
                shop_price.remove("")
                user.add_to_cart(shop_price,ordered_food)
                # shop_name_price=user.chose_shop(shop_price)



            else:
                print("There is no food that u can order : ")


        except Exception as error:
            print(error)



# def write():
#     while True:
#         pass
        # obj=user.option()

        # print("Choose an option:\n1. Group chat\n2. Private chat\n")
        # option = input("Enter your choice (1/2): \n")
        #
        # if option == "1":
        #     clients=input("Enter client names separated by commas (e.g. John, Sarah):")
        #     message = input("Enter your message ")
        #     message = f"Group Chat /{clients}/{name}:{message}"
        #     client.send(message.encode('ascii'))
        #
        # elif option == "2":
        #     client_name=input("Enter client name:")
        #     message = input("Enter your message: ")
        #     message = f"Private Chat ({client_name}): {message}"
        #     client.send(message.encode('ascii'))
        #
        # else:
        #     print("Invalid option! Please enter a valid choice.")

receive_thread = threading.Thread(target=receive)
receive_thread.start()
# write_thread = threading.Thread(target=write)
# write_thread.start()
