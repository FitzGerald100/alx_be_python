# Base class: Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Initialize the base class
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Initialize the base class
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition class: Library
class Library:
    def __init__(self):
        self.books = []  # List to store Book, EBook, and PrintBook instances

    def add_book(self, book):
        """
        Adds a book to the library. Ensures that the object is an instance of the Book class.
        """
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book}")
        else:
            print("Error: Only instances of Book (or subclasses) can be added to the library.")

    def list_books(self):
        """
        Lists all books in the library. If the library is empty, it notifies the user.
        """
        if not self.books:
            print("The library is currently empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)
