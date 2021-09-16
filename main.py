from datetime import datetime
from library_module.cons import ALLOWED_COMMANDS, MSG
from library_module.library import Biblioteka, Book
from library_module.person import User


bib = Biblioteka(address="Warszawa", name="Moja Biblioteka")

while True:
    command = input("Podaj komende: ")
    if command not in ALLOWED_COMMANDS:
        print(f"{MSG} Dostępne komendy: {ALLOWED_COMMANDS}")
        continue
    if command == 'stop':
        break
    if command == 'add':
        bib.add_book()
    if command == 'delete':
        bib.delete_book()
    if command == 'books':
        bib.show_books()
    if command == 'users':
        bib.show_users()
    if command == 'add_user':
        bib.add_user()
    if command == 'get_book':
        bib.get_book()
    if command == 'del_book':
        bib.del_book()
    if command == 'book_status':
        bib.get_book_status()