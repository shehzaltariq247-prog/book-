from book import Book  # import book class
from user import User  # import user class


class Library:
    def __init__(self):
        self.books = []  # list of books are created
        self.users = []  # list of users

    def add_book(self, isbn, title, author):
        for book in self.books:
            if book.isbn == isbn:
                print("book already added:")
                return
            else:
                self.books.append(Book(isbn, title, author))
                print("book added successfully:")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return
            else:
                print("book not founded.!")

    def search_book(self, keyword):
        for book in self.books:
            if book.isbn.lower() == keyword.lower():
                return
            elif book.title.lower() == keyword.lower():
                return
            elif book.author.lower() == keyword.lower():
                return

        print("book not founded.!")

    def register_users(self, user_id, user_name, membership):
        for user in self.users:
            if user.user_id == user_id:
                print("user excists")
                return
            else:
                self.users.append(User(user_id, user_name, membership))
                print("user is added successfully.!")

    def view_profile(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                user.display()
                return
            else:
                print("user not founded.")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
            else:
                return None

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
            else:
                return None

    def issue_book(self, isbn, user_id):
        user = self.find_user(user_id)
        book = self.find_book(isbn)
        if user is None:
            print("no users exist")
            return
        if book is None:
            print("no book exists.")
            return
        if not book.availabe:
            print("book is borrowed.")
        if not user.can_borrow():
            print("limit has been reached.!")
            return

        book.borrow()
        user.borrow_books.append(book)

        print("book issued successfully.")
    # return book

    def return_book(self, user_id, isbn):
        user = self.find_user(user_id)
        book = self.find_book(isbn)
        if book is None and user is None:
            print("invalid user and book.!")
            return
        if book not in user.borrow_books:
            print("user did not borrow this book")
            return
        user.borrow_books.remove(book)
        book.return_book()

        print("book returned successfully.")

    def inventory(self):
        if len(self.books) == 0:
            print("no books are added in library:")
            return
        for book in self.books:
            book.display()

    def active_loans(self):
        found = False
        for user in self.users:
            for book in self.books:
                print(f"title: {book.title} Borrowed by: {user.name}")
        if not found:
            print("no active loans")
