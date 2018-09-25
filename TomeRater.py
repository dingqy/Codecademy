class User(object):
    def __init__(self, name, email):  # unlimited type
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return print("The email has been successfully updated")

    def __repr__(self):
        temp = ""  # the output type of book
        for i in self.books.keys():
            temp = temp + "{} (rating: {})\n".format(i, self.books.get(i))
        return "User: {}   Email: {}   \nBooks read: \n{}".format(self.name, self.email, temp)

    def __eq__(self, other_user):
        if self.name == other_user.name & self.email == other_user.email:
            return True
        return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0
        none_num = 0
        for i in self.books:
            if self.books[i] is not None:
                total_rating += self.books[i]
            else:
                none_num += 1
        total_rating = total_rating / (len(self.books) - none_num)
        return total_rating


class Book(object):
    def __init__(self, title, isbn):  # unlimited type
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, address):
        self.isbn = address
        return print("The ISBN has been successfully updated")

    def add_rating(self, rating):
        if 4 >= rating >= 0:
            self.ratings.append(rating)
            return print("The rating has been successfully updated")
        else:
            return print("Invalid Rating")

    def __eq__(self, other):
        if self.title == other.title & self.isbn == other.isbn:
            return True
        return False

    def get_average_rating(self):
        total_rating = 0
        none_num = 0  # the number of None
        for i in self.ratings:
            if self.ratings is not None:
                total_rating += i
            else:
                none_num += 1
        average_rating = total_rating / (len(self.ratings) - none_num)
        return average_rating

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "Title: {}  ISBN: {}".format(self.title, self.isbn)


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "Title: {}  ISBN: {}  Author: {}".format(self.title, self.isbn, self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.level = subject
        self.subject = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "Title: {}  ISBN: {}  Level: {}  Subject: {}".format(self.title, self.isbn, self.level, self.subject)


class TomeRater(object):
    def __init__(self):
        self.users = {}  # key is email, value is User object
        self.books = {}  # key is Book object, value is the times the book was read
        self.isbn = []

    # I don't know what should be output when print TomeRater object.
    """   def __repr__(self):
        temp_user = ""
        temp_book = ""
        for i in self.users.keys():
            temp_user += "{}   ".format(self.users.get(i).name)
        for i in self.books.keys():
            temp_book += "{}   ".format(i.get_title)
        temp = "User who have read book: {}\nThe books that have been read: {}".format(temp_user, temp_book)
        return temp
    """

    def create_book(self, title, isbn):
        if isbn not in self.isbn:
            self.isbn.append(isbn)
            return Book(title, isbn)
        else:
            print("The ISBN of book can not be the same. Please choose another one")
            exit(0)

    def create_novel(self, title, author, isbn):
        if isbn not in self.isbn:
            self.isbn.append(isbn)
            return Fiction(title, author, isbn)
        else:
            print("The ISBN of book can not be the same. Please choose another one")
            exit(0)

    def create_non_fiction(self, title, subject, level, isbn):
        if isbn not in self.isbn:
            self.isbn.append(isbn)
            return Non_Fiction(title, subject, level, isbn)
        else:
            print("The ISBN of book can not be the same. Please choose another one")
            exit(0)

    def add_book_to_user(self, book, email, rating=None):
        temp = False
        for i in self.users:
            if i == email:
                self.users.get(i).read_book(book, rating)
                if rating is not None:
                    book.add_rating(rating)
                if book not in self.books:
                    self.books[book] = 1
                else:
                    self.books[book] = self.books.get(book) + 1
                temp = True
                break
        if not temp:
            return print("No user with email {}".format(email))

    def add_user(self, name, email, user_books=None):
        try:
            if "@" not in email:
                raise NameError
            if (".com" in email or ".edu" in email or ".org" in email) is False:
                raise NameError
            temp = User(name, email)  # new User object
            for i in self.users.keys():
                if email == i:
                    raise NameError
            self.users[email] = temp
            if user_books is not None:
                for i in user_books:
                    self.add_book_to_user(i, email)
        except NameError:
            print("Please choose another email address")

    def print_catalog(self):
        for i in self.books.keys():
            print("{}\n".format(i))

    def print_users(self):
        for i in self.users.values():
            print("{}".format(i))

    def most_read_book(self):
        maximum_value = 0
        for i in self.books:
            if self.books.get(i) > maximum_value:
                maximum_value = self.books.get(i)
                maximum = i
        return maximum

    def highest_rated_book(self):
        rating_value = 0
        for i in self.books:
            if i.get_average_rating() > rating_value:
                rating_value = i.get_average_rating()
                highest_rating = i
        return highest_rating

    def most_positive_user(self):
        rating_value = 0
        for i in self.users.keys():
            if self.users.get(i).get_average_rating() > rating_value:
                rating_value = self.users.get(i).get_average_rating()
                highest_rating = self.users.get(i).name
        return highest_rating

    # I don't know why the method __eq__ will have error
    """ def get_n_most_read_books(self, n):
        temp_books1 = self.books.items()
        temp_books = [[i[1], i[0]] for i in temp_books1]
        temp_books = sorted(temp_books)
        return temp_books
    """

    def get_n_most_prolific_readers(self, n):
        temp_users = sorted(self.users.values(), key=lambda user: len(user.books))
        i = n
        temp = "User name: {}  ".format(temp_users[n - 1].name)
        while len(temp_users[n - 1].books) == len(temp_users[i].books):
            temp += "{}  ".format(temp_users[i].name)
            if (i + 1) > len(temp_users) - 1:
                break
            i += 1
        return temp
