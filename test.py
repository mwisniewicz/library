from datetime import datetime
from library_module.library import Book
from library_module.person import User

book1 = Book(id=1, title="Pan T", author="Adam M")
book2 = Book(id=2, title="Pan A", author="Adam K")

book1.return_date = datetime(2021, 9, 1).date()
book1.get_date = datetime(2021, 9, 1).date()

book2.return_date = datetime(2021, 8, 30).date()
book2.get_date = datetime(2021, 8, 23).date()

user = User(id=1, first_name="Adam", last_name="Nowak")
user.books = [book1, book2]
print(user.calculate_penalties_price())