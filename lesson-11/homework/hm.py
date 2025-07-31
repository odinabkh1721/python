# Task 2 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Zero Division"
    return a / b


# 2

string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# 3

main.py

import math_operations
import string_utils

# Math functions
print(math_operations.add(5, 3))        
print(math_operations.divide(10, 0))     

# String functions
print(string_utils.reverse_string("hello"))       
print(string_utils.count_vowels("education"))     


geometry/circle.py

import math

def area(radius):
    return math.pi * radius ** 2

def circumference(radius):
    return 2 * math.pi * radius

from geometry import area, circumference

print(area(5))
print(circumference(5))

# 3

from geometry.circle import calculate_area, calculate_circumference

radius = 5

print(f"Aylananing yuzi: {calculate_area(radius):.2f}, uzunligi: {calculate_circumference(radius):.2f}")
