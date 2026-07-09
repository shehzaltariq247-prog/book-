class User:
    def __init__(self, user_id, user_name, membership):
        self.user_id = user_id
        self.user_name = user_name
        self.membership = membership
        self.borrow_books = []

    def borrow_limit(self):
        if self.membership.lower() == "student":
            return 3
        elif self.membership.lower() == "teacher":
            return 5

        return 2

    def can_borrow(self):
        return len(self.borrow_books) < self.borrow_limit()

    def display(self):
        print(
            f"user_id: {self.user_id} | user_name: {self.user_name} | membership: {self.membership}")

        if len(self.borrow_books) == 0:
            print("no books are to be borrowed:")
        else:
            print("books are borrowed:")
            for book in self.borrow_books:
                print(book.title)
