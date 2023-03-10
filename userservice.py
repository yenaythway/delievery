class UserService():
    def chose_food(self,avilable_food):
        print("########Avilable food#######")
        # avilable_food = ["BBQ", "Ar Pu Shr Pu", "Salad", "Fried chicken", "Mr lr shan kw", "Salad", "Hot Dog"]
        for i in avilable_food:
            print("-",i)
        ordered_food=input("Enter food name(include space) that u want to order : ").upper()
        for i in avilable_food:
            if i == ordered_food:
                return ordered_food

        else:
            print("There is no food that u enter")
            obj=UserService()
            return obj.chose_food(avilable_food)
    def chose_shop(self,shop_price):
        while True:
            print('-Shop->price')
            for i in range(0, len(shop_price), 2):
                print(f"-{shop_price[i]}->${shop_price[i + 1]}")
            shop_name = input("Enter shop name that u want to buy : ")
            for i in range(0, len(shop_price), 2):
                if shop_name == shop_price[i]:
                    qty = int(input("Enter qty : "))

                    price_qty=f"{shop_price[i+1]}/{qty}"
                    return price_qty
                    # amount = qty * shop_price[i + 1]
                    # while True:
                    #     user_money = int(input(f"Enter ${amount} for {qty}: "))
                    #     if user_money == amount:
                    #         s_name_money = f'{shop_name},{user_money},'
                    #         return s_name_money
                    #     print("Invalid amount")
            print("Invalid shop nmae")
    def take_bill(self):
        print("###########Cash Receipt#############\n"
              f"    Customer name : {'name'}\n"
              f"    Address       : {'address'}\n"
              f"    Phone Number  : {'phno'}\n"
              f"\n####################################\n"
              f"Product name    Price   Qty   Amount"
              )
        # for i in range(10):
        #     print(f"{product name}{price}{qty}{amount}")
        # print(cart)
    def add_to_cart(self,shop_price,oredered_food):#######
        cart = ''
        while True:
            user_shop_price = self.chose_shop(shop_price)
            cart = cart + user_shop_price
            op = input("Enter option:\n1 Cart again\n2 take bill")
            if op == '1':
                continue

            elif op == '2':
                print(cart)
                UserService.take_bill(cart)
                return 0

            print("Invalid")




obj=UserService()
# obj.option(["BBQ", "Ar Pu Shr Pu", "Salad", "Fried chicken", "Mr lr shan kw", "Salad", "Hot Dog"])
# obj.chose_shop(['May Khant Kaw', '$12', 'Shwe Nay Chi', '$12'])
obj.add_to_cart(['May Khant Kaw', 12, 'Shwe Nay Chi', 12],'HOT DOG')
