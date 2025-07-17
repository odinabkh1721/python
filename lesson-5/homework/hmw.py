
# Task 1 

def is_leap(year):
    if not isinstance(year, int):
         raise ValueError("Year must be an integer.")
         return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap(2024))  
print(is_leap(1900))  
print(is_leap(2000))  
print(is_leap(2023))  


# Task 2.2
 
n = int(input("Butun son kiriting"))
if n % 2 != 0:
     print ('Weird')

# Task 2.2 If n is even and in the inclusive range of 2 to 5, print Not Weird

n = int(input("Butun son kiriting"))
if n % 2 == 0 and 2 <= n <= 5:
     print ('Not Weird')

# Task 2.3 If n is even and in the inclusive range of 6 to 20, print Weird

n = int(input("Butun son kiriting"))
if n % 6 == 0 and  6 <= n <= 20:
     print ('Weird')

# Task 2.4 If n is even and greater than 20, print Not Weird


n = int(input("Butun son kiriting"))
if n % 2 == 0 and n<20:
     print ('Weird')


# Task 3 Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.


a = int(input("23","32","14"))
b = int(input("12","53","65"))

even_numbers = list(filter(lambda x: x % 2 == 0, range(a, b + 1)))
print("Juft sonlar:", even_numbers)


a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

even_numbers = list(filter(lambda x: x % 2 == 0, range(a, b + 1)))
print("Juft sonlar:", even_numbers)
