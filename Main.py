import sys
from Admin import Admin
from Library import Library

flag = True
l1 = Library("Ashwith")
print("Welcome to Library")
while flag:
    print("1.Login has a Admin")
    print("2.Add book")
    print("3.Search book by Id")
    print("4.Search book by Title")
    print("5.Search book by Author Name")
    print("6.BorrowBook")
    print("7.Remove Book")
    print("8.Sort By By Id")
    print("9.Sort By By Title")
    print("10.Sort By By Author Name")
    print("11.Sort By By Price")
    print("12.Return the book")
    print("13.Exit")

    try:
        choice = int(input("Enter the choice\n"))
        if choice == 1:
            Admin().admin_login()
        elif choice == 2:
            l1.add_book()
        elif choice == 3:
            book_id = int(input("Enter the id of the book\n"))
            l1.search_book_by_id(book_id)
        elif choice == 4:
            title = input("Enter the title of the book\n")
            l1.search_book_by_title(title)
        elif choice == 5:
            author = input("Enter the Author of the book\n")
            l1.search_book_by_author_name(author)
        elif choice == 6:
            l1.borrow_book()
        elif choice == 7:
            l1.remove_book()
        elif choice == 8:
            l1.sort_book_by_id()
        elif choice == 9:
            l1.sort_book_by_title_name()
        elif choice == 10:
            l1.sort_book_by_author_name()
        elif choice == 11:
            l1.sort_book_by_price()
        elif choice == 12:
            l1.return_book()
        elif choice == 13:
            print("Thank you for visiting our library")
            sys.exit()
    except (Exception, ValueError):
        print("Sorry this option not found")
