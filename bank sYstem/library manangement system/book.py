class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True

    def display(self):
        if self.available:
            status = "issued"
        else:
            status = "borrowed"

            print(
                f"isbn: {self.isbn} | title: {self.title} | author: {self.author} | status: {status}")
