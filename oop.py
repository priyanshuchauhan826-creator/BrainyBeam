# Class 1
class Student:
    def _init_(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def get(self):
        print("Student:", self.name, self.age, self.city)

    def post(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


# Class 2
class Employee:
    def _init_(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def get(self):
        print("Employee:", self.name, self.salary, self.department)

    def post(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department


# Class 3
class Product:
    def _init_(self, pname, price, quantity):
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def get(self):
        print("Product:", self.pname, self.price, self.quantity)

    def post(self, pname, price, quantity):
        self.pname = pname
        self.price = price
        self.quantity = quantity


# 2 Objects of Student
s1 = Student("Priyanshu", 17, "Ahmedabad")
s2 = Student("Rahul", 18, "Surat")

# 2 Objects of Employee
e1 = Employee("Amit", 30000, "IT")
e2 = Employee("Ravi", 25000, "HR")

# 2 Objects of Product
p1 = Product("Laptop", 50000, 5)
p2 = Product("Mouse", 500, 20)

# Get Data
s1.get()
s2.get()
e1.get()
e2.get()
p1.get()
p2.get()

print("\nAfter Update:\n")

# Update Data using post()
s1.post("Priyanshu Kumar", 18, "Vadodara")
e1.post("Amit Shah", 35000, "Software")
p1.post("Gaming Laptop", 60000, 3)

# Get Updated Data
s1.get()
e1.get()
p1.get()