from .person import User
from datetime import datetime
from datetime import timedelta
import os

class Biblioteka:
    """ Klasa reprezentująca bibliotekę,
    która grupuje książki i użytkowników """
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.users = []

    def show_books(self):
        if not self.books:
            print('Pusta baza książek!')
        else:
            print(self.books)

    def add_book(self):
        title = input("Tytuł: ")
        author = input("Autor: ")
        id = self.set_book_id()
        book = Book(id=id, title=title, author=author)
        self.books.append(book)
        print(f"Książka {book} dodana do bazy!")

    def delete_book(self):
        id = int(input("Podaj ID książki do usunięcia: "))
        for index, book in enumerate(self.books):
            if id == book.id:
                del self.books[index]
                del book

    def get_book(self):
        book_id = int(input("Podaj ID książki: "))
        book_ = self.get_available_book_by_id(book_id)
        if not book_:
            print("Książki nie ma w bazie!")
        else:
            user_id = int(input("Podaj ID użytkownika: "))
            user_ = self.get_user_by_id(user_id)
            if not user_:
                print("Brak użytkownika w bazie!")
            else:
                user_.books.append(book_)
                book_.user = user_
                book_.status = 'unavailable'
                book_.get_date = datetime.now().date()
                book_.return_date = book_.get_date + timedelta(days=14)
                print(f"{user_} wypożycza książkę {book_}")

    def del_book(self):
        user_id = int(input("Podaj ID użytkownika: "))
        user_ = self.get_user_by_id(user_id)
        if not user_:
            print("Brak użytkownika w bazie!")
        else:
            book_id = int(input("Podaj ID książki: "))
            book_ = self.get_user_book_by_id(book_id, user_)
            if book_:
                user_.books.remove(book_)
                book_.status = 'available'
                book_.user = None
                book_.get_date = None
                book_.return_date = None
                print(f"{user_} zwraca książkę {book_}")
            else:
                print(f"Brak książki w bazie!")

    def get_book_by_id(self, id):
        for index, book in enumerate(self.books):
            if id == book.id:
                return book
        return None

    def get_user_book_by_id(self, id, user):
        for index, book in enumerate(user.books):
            if id == book.id:
                return book
        return None

    def get_available_book_by_id(self, id):
        book_id_ = self.get_book_by_id(id)
        if book_id_ and book_id_.status == 'available':
            return book_id_
        return None

    def get_user_by_id(self, id):
        for index, user in enumerate(self.users):
            if id == user.id:
                return user
        return None

    def add_user(self):
        first_name = input("Imię: ")
        last_name = input("Nazwisko: ")
        id = self.set_user_id()
        user = User(id=id, first_name=first_name, last_name=last_name)
        self.users.append(user)
        print(f"Użytkownik {user.first_name} {user.last_name} dodany do bazy!")

    def set_book_id(self):
        if not self.books:
            return 1
        max_id = 0
        for book in self.books:
            if book.id > max_id:
                max_id = book.id
        return max_id + 1

    def set_user_id(self):
        if not self.users:
            return 1
        max_id = 0
        for user in self.users:
            if user.id > max_id:
                max_id = user.id
        return max_id + 1

    def show_users(self):
        if not self.users:
            print('Pusta baza użytkowników!')
        else:
            print(self.users)

    def get_book_status(self):
        book_id = int(input("Podaj ID książki: "))
        book = self.get_book_by_id(book_id)
        if book.user:
            message = f'''
            Książkę wypozyczyl {book.user}
            Książke oddajemy za {book.days_to_return()} dni
            '''
            print(message)
        else:
            print("Książka dostępna!")

class Book:
    
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.status = 'available'
        self.user = None

        self.return_date = None
        self.get_date = None

    def __str__(self):
        return f"({self.id}) {self.title} - {self.author} {(self.status)}"

    def __repr__(self):
        return f"({self.id}) {self.title} - {self.author} {(self.status)}"

    def days_to_return(self):
        date_delta = self.return_date - datetime.now().date()
        return date_delta.days