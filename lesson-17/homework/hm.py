import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

def rename_func(col):
    return col.lower().replace(" ", "_")

df = df.rename(columns=rename_func)

print(df)

# 2Question 

import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

def rename_func(col):
    return col.lower().replace(" ", "_")

df = df.rename(columns=rename_func) 
print(df.head(3)) # type: ignore

# 3 Find the mean age of the individuals

import pandas as pd

data = {
    'age': [25,30,35,40]
}
df = pd.DataFrame(data)

mean_age = df["age"].mean()
print("Mean age:", mean_age)

# 4 Select and print only the 'Name' and 'City' columns

import pandas as pd 

data ={
    'Name':['Alice','Bob','Charlie','David'],
    'City':['New York','Bob','Chalie','David']
}

df = pd.DataFrame(data)

result =df[["Name","City"]]
print(result)


# 5 Add a new column 'Salary' with random salary 
    
import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

df["Salary"] =[50000,40000,25000,9000]
print(df)

# 6 Display summary statistics of the DataFrame

import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago'],
    "Salary": [50000,40000,25000,9000]
}

df = pd.DataFrame(data)

print(df.describe())


# Homework 2  

import pandas as pd 

data = {
    'Month':['Jan','Feb','Mar','Apr'],
    'Sales':[5000,6000,7500,8000],
    'Expenses':[300,3500,4000,4500]
}

df = pd.DataFrame(data)
print(df)


# 2 Calculate and display the maximum sales and expenses.

import pandas as pd 

data = {
    'Sales':[5000,6000,7500,8000],
      'Expenses':[300,3500,4000,4500]
}

df = pd.DataFrame(data)

max_sales = df["Sales"].max()
max_expenses = df["Expenses"].max()

print(max_sales)
print(max_expenses)

3 Calculate and display the minimum sales and expenses.


import pandas as pd 

data = {
    'Sales':[5000,6000,7500,8000],
      'Expenses':[300,3500,4000,4500]
}

df = pd.DataFrame(data)

min_Sales = df["Sales"].min()
min_Expenses = df["Expenses"].min()

print(min_Sales)
print(min_Expenses)


# 4 Calculate and display the average sales and expenses.


import pandas as pd

data = {
    'Sales':[5000,6000,7500,8000],
      'Expenses':[300,3500,4000,4500]
}

df = pd.DataFrame(data)

mean_Sales = df["Sales"].mean()
mean_Expenses = df["Expenses"].mean()

print(mean_Sales)
print(mean_Expenses)


# Homework 3

# 1 Create a DataFrame named expenses with columns 'Category', 
# 'January', 'February', 'March', and 'April', representing 
# monthly expenses for different categories. Use below table.
    
import pandas as pd

data = {
    'Category':['Rent','Utilities','Groceries','Entertainmen'],
    'January':[1200,200,300,150],
    'February':[1300,220,320,160],
    'March':[1400,240,330,170],
    'April':[1500,250,350,180]
# }

df = pd.DataFrame(data)
print(df)

# 2Calculate and display the maximum expense for each category.

import pandas as pd 

data = {
    'Category': ['Rent','Utilities','Groceries','Entertainmen'],
    'Expenses': [1200, 300, 450, 200]
}

df = pd.DataFrame(data)

print("Maximum Expense:", df["Expenses"].max())

# 3 Calculate and display the minimum expense for each category.
    
import pandas as pd 

data = {
    'Category': ['Rent','Utilities','Groceries','Entertainmen'],
    'Expenses': [1200, 300, 450, 200]
}

df = pd.DataFrame(data)
 
min_expenses = df.groupby("Category")["Expenses"].min()

print("Minimum expense for each category:")
print(min_expenses)

4 Calculate and display the average expense for each category.
    
import pandas as pd 

data = {
    'Category': ['Rent','Utilities','Groceries','Entertainmen'],
    'Expenses': [1200, 300, 450, 200]
}

df = pd.DataFrame(data)

mean_expenses = df.groupby("Category")["Expenses"].mean()

print("Mean expenses for eache category:")
print(mean_expenses)
