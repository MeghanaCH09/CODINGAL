class library: 
    def __init__(self, list, name): 
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self): 
        print(f"We have the following books in our library: {self.name}")
        for book in shelf.booksList: 
            print(book)

    def lendBook(self, user, book): 
        if book not in self. lendDict.keys(): 
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else: 
            print(F"Book is already being used by {self.lendDict[Book]}")
        
        if __name == '__name__': 
            books = Library (['Python', 'Rich and Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS', "Ley's Upskill"])

            while(True):
                print(F"Welcome to the {books.name} library. Enter your choice to continue")
                print("1. Display Books")
                print("2. Lend a book")
                print("3. Add a book")
                print("4. Return a Book")
                user_choice = input()
                if user_choice not in ['1', '2', '3', '4',]: 
                    print("Please enter a valid option")
                    continue 

                if user_choice == 1:
                    books.displayBooks()
                
                else: 
                    book == input("Enter the name of the book you want to lend:")
                    user = input("Enter your name")
                    books.LendBook(user, book)