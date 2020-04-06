class Book:
    book_count = 1

    def __init__(self, book_id, title, author_name, price):
        Book.book_count += 1
        self.__bookId = int(book_id)
        self.__title = title
        self.__authorName = author_name
        self.__price = price
        self.available = True
        self.__sql = 0
        self.__value = 0
        self.list1 = list()

    @property
    def get_book_id(self):
        return self.__bookId

    @property
    def get_title(self):
        return self.__title

    @get_book_id.setter
    def set_title(self, title):
        self.__title = title

    @property
    def get_author_name(self):
        return self.__authorName

    @get_author_name.setter
    def set_author_name(self, author_name):
        self.__authorName = author_name

    @property
    def get_price(self):
        return int(self.__price)

    @get_price.setter
    def set_price(self, price):
        self.__price = price

    @property
    def get_available(self):
        return self.available

    # def __eq__(self, o: object) -> bool:
    #     return super().__eq__(o)

    @get_available.setter
    def set_available(self, available):
        self.available = available

    def __repr__(self) -> str:
        return super().__repr__()

    def display(self):
        print("BookId=", self.__bookId, "\n")
        print("Title=", self.__title, '\n')
        print("AuthorName=", self.__authorName, "\n")
        print("Price=", self.__price, '\n')

    def __hash__(self) -> int:
        return super().__hash__()

    # def __str__(self) -> str:
    #   return super().__str__()

    def __str__(self):
        return "BookId={} Title={} AuthorName={} Price={}".format(self.__bookId, self.__title, self.__authorName,
                                                                  self.__price)

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return self.__bookId == other.__bookId and self.__title == other.__title and self.__authorName == self.__author
        Name and self.__price == other.__price

    def __ne__(self, other):
        return (self.__bookId, self.__title, self.__authorName, self.__price) != (other.__bookId, other.__title, other.
                                                                                  __authorName, other.__price)

    def __lt__(self, other):
        return (self.__bookId, self.__title, self.__authorName, self.__price) < (other.__bookId, other.__title, other.
                                                                                 __authorName, other.__price)

    def __le__(self, other):
        return (self.__bookId, self.__title, self.__authorName, self.__price) <= (other.__bookId, other.__title, other.
                                                                                  __authorName, other.__price)

    def __gt__(self, other):
        return (self.__bookId, self.__title, self.__authorName, self.__price) > (other.__bookId, other.__title, other.
                                                                                 __authorName, other.__price)

    def __ge__(self, other):
        return (self.__bookId, self.__title, self.__authorName, self.__price) >= (other.__bookId, other.__title, other.
                                                                                  __authorName, other.__price)
# b1 = Book()
# b1.addbook()
# b1.display()
# b2 = Book()
# b2.addbook()
# b2.getbookid()
# b2.getauthorname()
# b2.gettitle()
# b2.getprice()
# b2.display()
# b2.setauthorname("ashwith")
# b2.display()
