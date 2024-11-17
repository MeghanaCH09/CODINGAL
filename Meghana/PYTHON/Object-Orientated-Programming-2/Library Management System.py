class Library:
    def __init__(self, books):
        self.books=books
        print("Welcome To The Library")

    def display_books(self):
        print("Books available in the library at the moment are:")
        for book in self.books:
            print(book)
        print()
    
    def lend_books(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f"You have borrowed {book}, Enjoy reading!")
        else:
            print("The book you want is currently no available, Sorry...")

    def return_books(self,book):
        self.books.append(book)
        print("Thank you for returning the book, Hope you enjoyed it...")
    
    def add_book(self,book):
        self.books.append(book)
        print(f"The book {book} has been added to the library")
    
    def __del__(self):
        print("Thank you for visiting our Library...Come again...")

library=Library(["Five Survive", "Caraval", "Harry Potter", "Sherlock Homes"])

library.display_books()

library.lend_books("Five Survive")

library.return_books("Five Survive")

library.add_book("Hunger Games")

library.display_books()