class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def issue_book(self):
        if not self.issued:
            self.issued = True
            print("Book ",self.title," issued successfully.")
        else:
            print("Book ",self.title," is already issued and unavailable.")

    def return_book(self):
        if self.issued:
            self.issued = False
            print("Book ",self.title," returned successfully.")
        else:
            print("Book ",self.title," was not issued.")

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = Book(title, author)
            print("Book ",title," added to the library.")
        else:
            print("Book ",title," already exists.")

    def issue_book(self, title):
        if title in self.books:
            self.books[title].issue_book()
        else:
            print("Book ",title," not found in the library.")

    def return_book(self, title):
        if title in self.books:
            self.books[title].return_book()
        else:
            print("Book ",title," not found in the library.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable books in the library:")
            for book in self.books.values():
                status = "Available" if not book.issued else "Issued"
                print("Title:",book.title,"Author:",book.author,"Status:",status)
        print()

def menu():
    library = Library()
    
    while True:
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("Enter book title to issue: ")
            library.issue_book(title)
        elif choice == '3':
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
