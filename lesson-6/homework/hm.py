# # Task 1 

def insert_underscore(txt):
     result = ""
     count = 0
     i = 0

     while i < len(txt):
         result += txt[i]
         count += 1
      if count == 3 and i + 1 < len(txt):
             if txt[i] not in "aeiouAEIOU" and txt[i + 1] != "_":
                 result += "_"
             else:
                 if i + 2 < len(txt):
                     result += txt[i + 1] + "_"
                     i += 1
             count = 0

         i += 1

     return result
print(insert_underscore("hello"))


# Task 2

n = 5

for i in range(n):
     print(i ** 2)

# Task 3

count = 1
while count <= 10:
     print(count)
     count +=1

# Task 2


for i in range(1, 6):         
     for j in range(1, i + 1): 
         print(j, end=' ')
     print() 


# Task 3

n = int(input("Son kiriting: "))
sum = 0

for i in range(1, n + 1):
     sum += i

print("Sum is:", sum)

# Task 4

n = int(input("Son kiriting: "))

for i in range(1, 11):
     print(n * i)

# Task 5 

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
     if num > 100 and num < 500:
         print(num)


# Task 6 


num = 75869
count = 0

while num > 0:
     num = num // 10
     count += 1
     print("Digit count is",count)


# Task 7 

for i in range(5, 0, -1):          #
     for j in range(i, 0, -1):      
         print(j, end=' ')
     print()  


# Task 8 

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
     print(list1[i])


# Task 9

for i in range(-10, 0):
    print(i)


# Task 10

for i in range(5): 
    print(i)

print("Done")

# Task 11

for num in range(25, 51):
     if num > 1:
         for i in range(2, int(num ** 0.5) + 1):
             if num % i == 0:
                 break
         else:
             print(num)


# Task 12

n_terms = 10

a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n_terms):
     print(a, end=' ')
     a, b = b, a + b


# Task 13

num = int(input("Son kiriting: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")
