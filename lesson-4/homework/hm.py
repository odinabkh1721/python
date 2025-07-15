# 1 Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict_desc = {'22','26','92','12'}
print ("Decending:",my_dict_desc)

my_dict_asc = {'22','26','92','12'}
print ("Ascending:",my_dict_asc)



#   2 Write a Python script to add a key to a dictionary.

my_dict = {'0','10','1','20'}
my_dict.update('20','2')
print (my_dict)
           

# 3 Write a Python script to concatenate the following dictionaries to create a new one.

my_dict = {'a': '2', 'b': '55', 'c': '56', 'd': '62'}
my_dict2 = {'e': '76', 'f': '74', 'g': '91'}
my_dict3 = {'h': '21', 'i': '63'}

concatenationd = {}

concatenationd.update(my_dict)
concatenationd.update(my_dict2)
concatenationd.update(my_dict3)

print(concatenationd)


# 4  Write a Python script to generate and print a dictionary that contains a number 
# (between 1 and n) in the form (x, x*x).

n = int(input(" 5: "))

squares_dict = {}

for x in range(1, 5 + 1):
 squares_dict[x] = x * x

print(squares_dict)

# 5 Write a Python script to print a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are the square of the keys.

squares_dict = {}

for x in range(1, 16): 
 squares_dict[x] = x * x

print(squares_dict)


# SET EXRERCISE
#1 Write a Python program to create a set.

first_set = {'one', 'two', 'three', 'four'}
second_set = {'banana', 'orange', 'peach'}

result = first_set.union(second_set)
print(result) 

# 2 Write a Python program to iterate over sets.

my_set = {'banana','orange','strawberry','peach'}
for fruit in my_set:
 print(fruit)

# 3 Write a Python program to add member(s) to a set.
my_set = {'Odina','Mubina','Mushtariy','Muhamadiyor'}
my_set.add('Mehrinoz')
print(my_set)

# 4 Write a Python program to remove item(s) from a given set.

my_set ={'book','notbook','pen','phone'}
my_set.remove('phone')
print(my_set)

# 5 Write a Python program to remove an item from a set if it is present in the set.

my_set = {'world','depression','life','act','goal'}
my_set.remove('world')
print (my_set)
