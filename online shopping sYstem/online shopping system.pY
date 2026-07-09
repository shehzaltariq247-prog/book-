class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        class shopping_cart:
            def __init__(self):
                self.items = []
                def add_item(self, product):
                    self.items.append(product)
                    def print_cart(self):
                        for x in self.items:
                            print(f"Product Name: {x.name}, Price: {x.price}")

                            p1 = product("Laptop", 1000)
                            p2 = product("Smartphone", 500)
                            c1 = shopping_cart()
                            c2.add_item(p1)
                            c2.add_item(p2)
                            c2.print_cart()