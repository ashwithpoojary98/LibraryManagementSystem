from Book import Book
from operator import attrgetter
from Admin import Admin


class Library:
    list1 = []

    def __init__(self, library_name):
        self.name = library_name
        self.title = None
        self.author_name = None
        self.price = None
        self.bid = 0
        self.b1 = None

    def add_book(self):
        if Admin().admin_login():
            self.bid = int(Book.book_count)
            self.title = input("Enter the Book Title\n")
            self.author_name = input("Enter the Author name\n")
            self.price = int(input("Enter the Price\n"))
            self.b1 = Book(self.bid, self.title, self.author_name, self.price)
            print(self.b1)
            self.list1.append(self.b1)
            if len(self.list1) >= 1:
                print("Book Added Successfully")
            else:
                print("Sorry Book is not added to the library")

    def search_book_by_id(self, book_id):
        book_not_found = True
        for obj in self.list1:
            if obj.get_book_id == book_id:
                book_not_found = False
                print("Book is found")
                break
        if book_not_found:
            print("Book is not found")

    def search_book_by_title(self, title):
        book_not_found = True
        for obj in self.list1:
            if obj.get_title == title:
                book_not_found = False
                print("Book is found")
                break
        if book_not_found:
            print("Book is not found")

    def search_book_by_author_name(self, author_name):
        book_not_found = True
        for obj in self.list1:
            print(obj.get_author_name)
            if obj.get_author_name == author_name:
                book_not_found = False
                print("Book is found")
                break
        if book_not_found:
            print("Book is not found")

    def borrow_book(self):
        book_not_found = True
        book_id = int(input("Enter the book id\n"))
        for obj in self.list1:
            if obj.get_book_id == book_id:
                book_not_found = False
                if not obj.get_available:
                    print("Sorry Book is already borrowed")
                    break
                else:
                    ch = input("Enter Y/y to confirm\n")[0]
                    ch = ch.upper()
                    if ch == 'Y':
                        obj.display()
                        print("Book successfully Borrowed")
                        obj.set_available = False
                    else:
                        print("Sorry you not confirmed please try again")
        if book_not_found:
            print("Book is not found")

    def remove_book(self):
        if Admin().admin_login():
            book_not_found = True
            book_id = int(input("Enter the book id to remove the book\n"))
            for obj in self.list1:
                if obj.get_book_id == book_id:
                    self.list1.remove(obj)
                    book_not_found = False
                    obj.display()
                    print("Book is removed")
                    break
            if book_not_found:
                print("Your Enter book is not available")

    def return_book(self):
        book_not_found = True
        book_id = int(input("Enter the book id\n"))
        for obj in self.list1:
            if obj.get_book_id == book_id:
                obj.set_available = True
                book_not_found = False
                print("Book is Successfully returned")
                break
        if book_not_found:
            print("Sorry this book is not in this Library")

    def sort_book_by_id(self):
        s1 = sorted(self.list1)
        for i in range(0, len(s1)):
            print(s1[i])

    def sort_book_by_author_name(self):
        s1 = sorted(self.list1, key=attrgetter('get_author_name'))
        for i in range(0, len(s1)):
            print(s1[i])

    def sort_book_by_title_name(self):
        s1 = sorted(self.list1, key=attrgetter('get_title'))
        for l in range(0, len(s1)):
            print(s1[l])

    def sort_book_by_price(self):
        s1 = sorted(self.list1, key=attrgetter('get_price'))
        for i in range(0, len(s1)):
            print(s1[i])

    def __str__(self):
        return self.name
