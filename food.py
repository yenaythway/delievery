class Item:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Food(Item):
    def __init__(self, name, price, category, cuisine):
        super().__init__(name, price, category)
        self.cuisine = cuisine

class Drink(Item):
    def __init__(self, name, price, category, size):
        super().__init__(name, price, category)
        self.size = size

class Shop:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def get_menu(self):
        return self.menu

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

menu1 = [Food("Fried Chicken", 12.99, "Entree", "Southern"), Drink("Coffee", 2.99, "Beverage", "Medium")]
menu2 = [Food("Pizza", 15.99, "Entree", "Italian"), Drink("Soda", 1.99, "Beverage", "Large")]

shop1 = Shop("Southern Kitchen", menu1)
shop2 = Shop("Italian Pizzeria", menu2)

shops = [shop1, shop2]

print("Select a shop to order from:")
for index, shop in enumerate(shops):
    print(f"{index+1}. {shop.name}")
selection = int(input()) - 1
selected_shop = shops[selection]

menu = selected_shop.get_menu()
print("Menu:")
for item in menu:
    print(f"{item.name} - {item.price}")

print("Select an item to add to your order:")
for index, item in enumerate(menu):
    print(f"{index+1}. {item.name}")
selection = int(input()) - 1
selected_item = menu[selection]

order = Order()
order.add_item(selected_item)

print("Your order:")
for item in order.items:
    print(f"{item.name} - {item.price}")
print(f"Total: {order.get_total()}")
