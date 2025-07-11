# Task 1 Create a list containing five different fruits and print the third fruit

fruits_list = ['apple','banana','orange','strawberry','peach']
print(fruits_list[2])

# Task 2 Create two lists of numbers and concatenate them into a single list.

my_list =[1,3,8]
other_list =[4,8,4,1]
combined_list= my_list + other_list
print(combined_list)


# Task 3 Given a list of numbers, extract the first, middle, and last elements and store them in a new lis
numbers = [40,50,4,99,66,44,58,11]
first = numbers[0]
middle = numbers[len(numbers)// 2]
last = numbers [-1]

new_list = [first,middle,last]

print (new_list)

# Task 4 Create a list of your five favorite movies and convert it into a tuple.

movies = ["Exception","Moneyball","Moneyball","GameRole"]
converted = tuple(movies)
print(converted)

# Task 5

cities = ["London", "New York", "Tokyo", "Paris", "Berlin"]

if "Paris" in cities:
print("Paris is in the list.")
else:
print("Paris is not in the list.")


# Task 6

numbers = list('12567325')
numbers.reverse()
print(numbers)

# Task 7 Given a list of numbers, swap the first and last elements.

# numbers = ['11','23','18','44']
numbers[0], numbers[-1] = numbers[-1], numbers[-1]
    
print (numbers)

# Task 8 Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

numbers = tuple(range(1, 11)) 
print(numbers[3:8]) 

# Task 9

colors = ('blue','red','yellow')
colors.count('blue')
print(colors.count('blue'))

# Task 10 

animals = ('cat','dog','elephant','fox','lion')
print(animals.index('lion'))

# Task 11 Create two tuples of numbers and merge them into a single tuple.

numbers = ('11', '22', '12', '122', '55', '77')
other_numbers = ('77', '86', '98', '45', '77')

merged = numbers + other_numbers
print(merged)

# Task 12 Given a list and a tuple, find and print their lengths.

my_list = [10, 20, 30, 40, 50]
my_tuple = (1, 2, 3, 4)

print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))


# Task 13 Create a tuple of five numbers and convert it into a list.

numbers_tuple = (10, 20, 30, 40, 50)  
numbers_list = list(numbers_tuple)   
print(numbers_list)


# Task 14 

numbers = (15, 3, 27, 8, 42, 10)

max_value = max(numbers)
min_value = min(numbers)

print("Maximum value:", max_value)
print("Minimum value:", min_value)



# Task 15

words = ("apple", "banana", "cherry", "date", "elderberry")

reversed_words = words[::-1]

print(reversed_words)
