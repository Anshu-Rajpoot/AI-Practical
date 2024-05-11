books = {
    "001": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "ISBN": "978-0743273565",
        "publisher": "Scribner"},
    "002": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "ISBN": "978-0446310789",
        "publisher": "J. B. Lippincott & Co." },
    "003": {
        "title": "1984",
        "author": "George Orwell",
        "ISBN": "978-0451524935",
        "publisher": "Signet Classics"}}
def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    ISBN = input("Enter book ISBN: ")
    publisher = input("Enter book publisher: ")
    books[book_id] = {"title": title, "author": author, "ISBN": ISBN, "publisher": publisher}
    print("Book added successfully.")
def view_book():
    book_id = input("Enter book ID: ")
    if book_id in books:
        print(f"Title: {books[book_id]['title']}")
        print(f"Author: {books[book_id]['author']}")
        print(f"ISBN: {books[book_id]['ISBN']}")
        print(f"Publisher: {books[book_id]['publisher']}")
    else:
        print("Book not found.")
def search_book():
    query = input("Enter search query: ")
    found_books = []
    for book_id, book in books.items():
        if query in book.values():
            found_books.append(book_id)
    if found_books:
        for book_id in found_books:
            print(f"Title: {books[book_id]['title']}")
            print(f"Author: {books[book_id]['author']}")
            print(f"ISBN: {books[book_id]['ISBN']}")
            print(f"Publisher: {books[book_id]['publisher']}")
    else:
        print("No books found.")
def delete_book():
    book_id = input("Enter book ID: ")
    if book_id in books:
        del books[book_id]
        print("Book deleted successfully.")
    else:
        print("Book not found.")
def expert_system():
    while True:
        print("Welcome to the library!")
        print("Enter 1 to add a book.")
        print("Enter 2 to view a book.")
        print("Enter 3 to search for a book.")
        print("Enter 4 to delete a book.")
        print("Enter 5 to exit.")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
# Test the system
expert_system()
