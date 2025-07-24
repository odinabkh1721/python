
# Task 1

class Circle:
    def __init__(self,area,perimetr,math.pi):
        self.area = area 
        self.perimetr = perimetr
        self.math.are = math.area

        def get_info(self):
            return f"Circle:{self.area}\nperimetr: {self.math.area}\n"
        
        
res = Circle ('area','rectangle','pi.value')

print(res.get_info())











Task 1

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_info(self):
        return f"Circle radius: {self.radius}\nArea: {self.get_area():.2f}\nPerimeter: {self.get_perimeter():.2f}"


res = Circle(5)
print(res.get_info())


# Task 2

from datetime import datetime

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year

    def get_info(self):
        return f"Name: {self.name}\nCountry: {self.country}\nAge: {self.get_age()}"

res = Person("Ali", "Uzbekistan", 2005)

print(res.get_info())



# Task 3

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero"

calc = Calculator(10, 5)

print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())


# Task 4 


import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
    def perimeter(self):
        return 2 * math.pi * self.r

class Square(Shape):
    def __init__(self, a):
        self.a = a
    def area(self):
        return self.a ** 2
    def perimeter(self):
        return 4 * self.a

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c

c = Circle(3)
s = Square(4)
t = Triangle(3, 4, 5)

print("Circle area:", c.area())
print("Square area:", s.area())
print("Triangle perimeter:", t.perimeter())


# Task 5


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(current, value):
            if current is None:
                return Node(value)
            if value < current.value:
                current.left = _insert(current.left, value)
            elif value > current.value:
                current.right = _insert(current.right, value)
            return current

        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(current, value):
            if current is None:
                return False
            if current.value == value:
                return True
            elif value < current.value:
                return _search(current.left, value)
            else:
                return _search(current.right, value)

        return _search(self.root, value)
    
tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)

print(tree.search(5))   
print(tree.search(12))


# Task 

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def display(self):
        print("Stack:", self.items)

    def is_empty(self):
        return len(self.items) == 0
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()      
print(s.pop())    
s.display()      


# Task 

class Bank:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} so'm qo‘shildi.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi.")
        else:
            print("Yetarli pul yo‘q!")

    def check_balance(self):
        print(f"{self.name} hisobida: {self.balance} so'm")

client = Bank("Ali")
client.deposit(1000)
client.withdraw(300)
client.check_balance()
