class car:
    def __init__(self, brand, model, rent_price):
        self.brand = brand
        self.model = model
        self.rent_price = rent_price
        self.available = True

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}, Rent Price: ${self.rent_price}")

    def rent(self):
        if self.available:
            self.available = False
            print(f"{self.brand} {self.model} has been rented for ${self.rent_price}.")
        else:
            print(f"{self.brand} {self.model} is not available for rent.")

    def return_car(self):
        if not self.available:
            self.available = True
            print(f"{self.brand} {self.model} has been returned.")
        else:
            print(f"{self.brand} {self.model} was not rented.")


if __name__ == "__main__":
    c1 = car("honda", "civic", 200)
    c1.display_info()
    c1.rent()
    c1.return_car()
