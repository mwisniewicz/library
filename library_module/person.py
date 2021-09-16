class User:
    
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.books = []

    def __str__(self):
        return f'({self.id}) - {self.first_name} {self.last_name} [{self.books}]'

    def __repr__(self):
        return f'({self.id}) - {self.first_name} {self.last_name} [{self.books}]'

    def calculate_penalties_price(self):
        if self.books:
            days = 0
            for book in self.books:
                if book.days_to_return() < 0:
                    days = days - book.days_to_return()
            return days * 10.0
        return 0.0

class Administrator:
    
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password