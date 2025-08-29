# 1  Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.

import pandas as pd 

df = pd.read_csv("sales_data.csv")
print(df.columns)

data = {
    'Category':['Electronics','Clothing','Electronics','Home','Clothing'],
    'Quantity':['10','5','8','12','15']
}
df = pd.DataFrame(data)

total_quantity = df.groupby('Category')['Quantity'].sum().reset_index()

total_quantity.rename(columns={'Quantity': 'TotalQuantitySold'}, inplace = True)

print(total_quantity)


# 1 task Average price per unit.

import pandas as pd 

df = pd.read_csv("sales_data.csv")
print(df.columns)

data = {
    'Price':[800,20,400,50,30],
    'Product':['Laptop','T-Shirt','Smartphone','Cofee Maker','Jeans']
}

df = pd.DataFrame(data)

average_price = df.groupby('Product')['Price'].mean().reset_index()
average_price.rename(columns={'Price': 'AveragePrice'},inplace = True)

print(average_price)



# 1 task Maximum quantity sold in a single transaction.

import pandas as pd 

data = {
    'Date': ['2023-01-01','2023-01-01','2023-01-02','2023-01-02','2023-01-03'],
    'Product': ['Laptop','T-Shirt','Smartphone','Coffee Maker','Jeans'],
    'Category': ['Electronics','Clothing','Electronics','Home','Clothing'],
    'Quantity': [10,5,8,12,15],
    'Price': [800,20,400,50,30]
}

df = pd.DataFrame(data)

# Maximum quantity in a single transaction
max_quantity = df['Quantity'].max()
max_transaction = df.loc[df['Quantity'].idxmax()]

print("Maximum quantity sold in a single transaction:", max_quantity)
print("Transaction details:\n", max_transaction)

# 2 TASK Identify the top-selling product in each category based on the total quantity sold.

import pandas as pd 

data = {
    'Product':['Lptop','T-Shirt','Smartphone','Cofee Maker','Jeans'],
    'Category':['Electronics','Clothing','Electronics','Home','Clothing'],
    'Quantity':['10','5','8','12','15']
}

df = pd.DataFrame(data)

category_sales = df.groupby(["Category","Product"])["Quantity"].sum().reset_index()


top_products = category_sales.loc[category_sales.groupby("Category")["Quantity"].idxmax()]

print(top_products)



# 3 Task Find the date on which the highest total sales (quantity * price) occurred.

import pandas as pd 

data = {
    'Date':['2023-01-01','2023-01-01','2023-01-02','2023-01-02','2023-01-03'],
    'Quantity':[10,5,8,12,15],   # int qilib oldik
    'Price':[800,20,400,50,30]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Quantity"] * df["Price"]

date_sales = df.groupby("Date")["Total_Sales"].sum().reset_index()

top_date = date_sales.loc[date_sales["Total_Sales"].idxmax()]

print(date_sales)
print("\nEng katta savdo bo‘lgan sana:")
print(top_date)


# hometask 2 

import pandas as pd 

df = pd.read_csv("customer_csv")

print(df.head())


#1 task Group the data by CustomerID and filter out customers who have made less than 20 orders.

import pandas as pd

data = {
    'CustomerID':['101','102','103','101','102'],
     'Quantity':[1,2,3,2,1],
     'Product':['Laptop','Headphones','Smartphones','External Hard Drive','Backpack'],
     'OrderID':[1,2,3,4,5]
}

df = pd.DataFrame(data)



less_than = df.groupby('CustomerID')['OrderID'].count()
filtered = less_than[less_than < 20]

print(filtered)

# Task 2 Identify customers who have ordered products with an average price per unit greater than $120.

import pandas as pd 

data = {
    'CustomerID':[101,102,103,101,102],
    'Price':[800,150,400,80,40],
    'OrderID':[1,2,3,4,5]
}

df = pd.DataFrame(data)

ordered = df.groupby('CustomerID')['Price'].mean()
filtered = ordered[ordered > 120]

print(filtered)



# Task 3 Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.


import pandas as pd 

data = {
    'Quantity':[2,1,3,2,1],
    'Products':['Laptop','Headphones','Smartphone','External Hard Drive','Backpack'],
    'Price':[800,50,600,120,40]
}

df = pd.DataFrame(data)

totals = df.groupby("Products").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Price=("Price", "sum")
).reset_index()

filtered = totals[totals["Total_Quantity"] < 5]

print(filtered)





