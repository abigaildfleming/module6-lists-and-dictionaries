class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print("{} {} @ ${:.2f} = ${:.2f}".format(self.item_name, self.item_quantity, self.item_price, self.item_quantity * self.item_price))

    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.cart_items = []
        self.customer_name = customer_name
        self.current_date = current_date

    def add_item(self, item_obj):
        self.cart_items.append(item_obj)

    def remove_item(self, item):
        count = 0
        for i in range(len(self.cart_items) - 1):
            if self.cart_items[i].item_name == item:
                del self.cart_items[i]
                count += 1
                break
        if count == 0:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_obj):
        for cart_item in self.cart_items:
            if cart_item.item_name == item_obj.item_name:
                if item_obj.item_price is not None:
                    cart_item.item_price = item_obj.item_price
                if item_obj.item_quantity is not None:
                    cart_item.item_quantity = item_obj.item_quantity
                if item.item_description is not None:
                    cart_item.item_description = item_obj.item_description
            else:
                print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total = 0
        for x in self.cart_items:
            total += x.item_quantity
        return total

    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            total_cost += i.item_price * i.item_quantity
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("{}\'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("SHOPPING CART IS EMPTY\n")
        else:
            print("{}\'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: {}".format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                item.print_item_cost()

            print("Total: ${:.2f}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("{}\'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

if __name__ == '__main__':
    def print_menu(cart):
        menu_options = {
            'a' : "Add item to cart",
            'r' : "Remove item from cart",
            'c' : "Change item quantity",
            'i' : "Output items' descriptions",
            'o' : "Output shopping cart",
            'q' : "Quit"
        }
        while True:
            print("\nMENU")
            for key, value in menu_options.items():
                print("{} - {}".format(key, value))
            print("\n")

            choice = input("Choose an option:\n")
            if choice == "q":
                break
            else:
                if choice in ["i", "o", "q"]:
                    if choice == "i":
                        print("OUTPUT ITEMS' DESCRIPTIONS")
                        cart.print_descriptions()

                    elif choice == "o":
                        print("OUTPUT SHOPPING CART")
                        cart.print_total()

                else:
                    choice = input("Choose an option:\n")

    name = input("Enter customer's name (ex. Abby Fleming):\n")
    date = input("Enter today's date (ex. December 23, 2023):\n")

    cart = ShoppingCart(name, date)

    num_items = 2
    total = 0
    for i in range(num_items):
        print('\nItem {}'.format(i + 1))
        item_name = input('Enter the item name (ex: apple, Chips): \n')
        item_price = float(input('Enter the item price (ex: 1, 2.38): \n'))
        item_quantity = int(input('Enter the item quantity (ex: 1, 2): \n'))
        item_description = input('Enter the item description: \n')
        item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        cart.add_item(item)

    print_menu(cart)








