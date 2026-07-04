class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"{product.name} has been added to cart.")

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)
            print(f"{product.name} removed from cart.")

            if not self.items:
                print("cart is empty.")


if __name__ == "__main__":
    cart_instance = cart()
    apple = product("Apple", 1.99)
    banana = product("Banana", 0.99)

    cart_instance.add_item(apple)
    cart_instance.add_item(banana)
    cart_instance.remove_item(apple)
    cart_instance.remove_item(banana)

