from library_module.cons import ALLOWED_COMMANDS, MSG
from library_module.library import Biblioteka

# books = [
#     {'id': 1, 'title': '', 'author': ''},
#     {'id': 2, 'title': '', 'author': ''},
# ]
books = []

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