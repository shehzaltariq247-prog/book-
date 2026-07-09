from library import Library


l1 = Library()


def get_number(message):
    while True:
        value = input(message).strip()

        if value == "":
            print("Input cannot be empty!")
        elif value.isdigit():
            return value
        else:
            print("Please enter numbers only!")


def get_name(message):
    while True:
        value = input(message).strip()

        if value == "":
            print("Input cannot be empty!")

        elif value.replace(" ", "").isalpha():
            return value

        else:
            print("Only alphabets are allowed!")


def get_membership():
    while True:
        membership = input("Membership (student/teacher): ").strip().lower()

        if membership == "":
            print("Membership cannot be empty!")

        elif membership in ["student", "teacher"]:
            return membership

        else:
            print("Enter only student or teacher!")


def get_choice():
    while True:
        choice = input("Enter your choice (1-10): ").strip()

        if choice == "":
            print("Choice cannot be empty!")

        elif choice.isdigit() and 1 <= int(choice) <= 10:
            return choice

        else:
            print("Invalid choice! Enter number between 1 and 10.")


def get_search():
    while True:
        value = input("Enter ISBN / Title / Author: ").strip()

        if value == "":
            print("Search field cannot be empty!")

        else:
            return value


while True:

    print("\n______ Library Management System ______")

    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Register User")
    print("5. View User Profile")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Show Inventory")
    print("9. Active Loans")
    print("10. Exit")

    choice = get_choice()

    if choice == "1":

        print("\n----- Add Book -----")

        isbn = get_number("ISBN: ")

        title = get_name("Title: ")

        author = get_name("Author: ")

        l1.add_book(isbn, title, author)

    elif choice == "2":

        print("\n----- Remove Book -----")

        isbn = get_number("ISBN: ")

        l1.remove_book(isbn)

    elif choice == "3":

        print("\n----- Search Book -----")

        keyword = get_search()

        l1.search_book(keyword)

    elif choice == "4":

        print("\n----- Register User -----")

        user_id = get_number("User ID: ")

        user_name = get_name("User Name: ")

        membership = get_membership()

        l1.register_users(user_id, user_name, membership)

    # VIEW PROFILE

    elif choice == "5":

        print("\n----- User Profile -----")

        user_id = get_number("User ID: ")

        l1.view_profile(user_id)

    # ISSUE BOOK

    elif choice == "6":

        print("\n----- Issue Book -----")

        isbn = get_number("ISBN: ")

        user_id = get_number("User ID: ")

        l1.issue_book(isbn, user_id)

    # RETURN BOOK

    elif choice == "7":

        print("\n----- Return Book -----")

        user_id = get_number("User ID: ")

        isbn = get_number("ISBN: ")

        l1.return_book(user_id, isbn)

    # INVENTORY

    elif choice == "8":

        print("\n----- Inventory -----")

        l1.inventory()

    # ACTIVE LOANS

    elif choice == "9":

        print("\n----- Active Loans -----")

        l1.active_loans()

    # EXIT

    elif choice == "10":

        print("\nThank you for using Library Management System!")

        break
