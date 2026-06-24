# Task Implementation

class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_details(self):
        print(f"Device: {self.brand} {self.model}, Price: ${self.price}")

    def post_update(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def get_info(self):
        print(f"Employee: {self.name}, Role: {self.role}, Salary: {self.salary}")

    def post_edit(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_data(self):
        print(f"Book: {self.title} by {self.author}, {self.pages} pages")

    def post_changes(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

# Creating 2 objects per class
d1 = Device("Apple", "iPhone 15", 999)
d2 = Device("Samsung", "S24", 899)

e1 = Employee("Alice", "Dev", 80000)
e2 = Employee("Bob", "Designer", 70000)

b1 = Book("1984", "George Orwell", 328)
b2 = Book("The Hobbit", "J.R.R. Tolkien", 310)

# Example usage:
d1.get_details()
d1.post_update("Apple", "iPhone 15 Pro", 1099)
d1.get_details()
