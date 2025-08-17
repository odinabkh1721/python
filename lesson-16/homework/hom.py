
# Task 16 
# question 1

import numpy as np

# Original list
my_list = [12.23, 13.32, 100, 36.32]
print("Original List:", my_list)

# Convert to NumPy array
arr = np.array(my_list)
print("One-dimensional NumPy array:", arr)

# question 2

import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)


# question 4 

import numpy as np

values = np.arange(12,38)
print(values)

# Question5

import numpy as np

my_list = [1,2,3,4]
print("original List",my_list)

# # Question 6

import numpy as np

# Sample array in Fahrenheit
fahrenheit = np.array([0, 12, 45.21, 34, 99.91, 32])
print("Values in Fahrenheit degrees:", fahrenheit)

# Convert to Celsius
celsius = (fahrenheit - 32) * 5/9
print("Values in Centigrade degrees:", np.round(celsius, 2))

# Convert back to Fahrenheit
f_back = celsius * 9/5 + 32
print("Values in Fahrenheit degrees:", np.round(f_back, 2))


# Question7

import numpy as np
my_list = [10,20,30]
print("Original array",my_list)

new_list = np.append(my_list,[40,50,60,70,80,90])
print("After append",new_list)


# Question8

import numpy as np

arr = np.random.randint(0, 100, 10)
print("Random Array:", arr)

mean_val = np.mean(arr)

median_val = np.median(arr)

std_val = np.std(arr)

print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_val)

# Question 9 

import numpy as np

arr = np.random.randint(0, 100, 10)
print("Random Array:", arr)

mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)
min_val = np.min(arr)
max_val = np.max(arr)

print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_val)
print("Minimum:", min_val)
print("Maximum:", max_val)

# Question 10 

import numpy as np

arr = np.random.rand(3, 3, 3)
print("3x3x3 Random Array:\n", arr)
