# book manangement sYstem
books = []
while True:
    print("1. Add book")
    print("2. View books")
    print("3. Search book")
    print("4. Exit")
    print("5. delete book")
    choice = input("enter choice (1-5):")
    if choice == "1":
        book_name = input("enter book name:")
        books.append(book_name)
        print("book added successfully!")
    elif choice == "2":
        if len(books) == 0:
            print("no books available.")
        else:
            print("books available:")
            for x in books:
                print(x)
    elif choice == "3":
        search_name = input("enter book name to search:")
        if search_name in books:
            print("book found!")
        else:
            print("book not found.")
    elif choice == "5":
        book_name = input("enter book name to delete:")
        if book_name in books:
            books.remove(book_name)
            print("book deleted successfully!")
        else:
            print("book not found.")
    elif choice == "4":
        print("exiting...")
        break
    else:
        print("invalid choice. please try again choice(1-5).")