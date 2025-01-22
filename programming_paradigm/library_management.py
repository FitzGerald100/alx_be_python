class Book:
    """A class representing a book in the library. """

    def __init__(self, title, author):

        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Marked the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """check if the book is available."""
        return not self._is_checked_out
    

class lIbrary:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        """Initialize a new library instance."""
        self.books = []

    def add_book(self, book):
        """add a new book to the library.
        
        :param book: An instance of the Book class."""

        self.books.append(book)

    def check_out_book(self, title):
         """
        Check out a book by its title.
        
        :param title: The title of the book to check out.
        :return: A message indicating success or failure.
        """
         for book in self._books:
             if book.title == title:
                 if book.check_out():
                     print(f"checked out: {title}")
                     return
                 else:
                     print(f"Error: '{title}' is already checked out.")
                     return
                 print(f"Error: Book titled '{title}' not found")
         

    def return_book(self, title):
         """
        Return a book by its title.
        
        :param title: The title of the book to return.
        :return: A message indicating success or failure.
        """
         
         for book in self._books:
             if book.title == title:
                 if book.return_book():
                     print(f"Returned: {title}")
                     return
                 else:
                     print(f"Error: '{title}' is not checked out")
                     return
             print(f"Error: Book titlr '{title}' not found.")

    def list_available_books(self):
        """List of books available with its titles"""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")
            
