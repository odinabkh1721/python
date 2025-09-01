import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

df1.columns = df1.columns.str.strip()

grade_cols = [c for c in df1.columns if c != 'Student_ID']

df1['Average_Grade'] = df1[grade_cols].mean(axis=1).round(2)

print(df1[['Student_ID', 'Average_Grade']])


import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

grade_cols = ['Math', 'English', 'Science']
df1['Average_Grade'] = df1[grade_cols].mean(axis=1).round(2)

print("Average grade for each student:")
print(df1[['Student_ID', 'Average_Grade']])

top_student = df1.loc[df1['Average_Grade'].idxmax()]

print("\nStudent with the highest average grade:")
print(top_student[['Student_ID', 'Average_Grade']])


import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

grade_cols = ['Math', 'English', 'Science']
df1['Average_Grade'] = df1[grade_cols].mean(axis=1).round(2)

top_student = df1.loc[df1['Average_Grade'].idxmax()]

df1['Total'] = df1[grade_cols].sum(axis=1)

print("Average grade for each student:")
print(df1[['Student_ID', 'Average_Grade']])

print("\nStudent with the highest average grade:")
print(top_student[['Student_ID', 'Average_Grade']])

print("\nTotal marks for each student:")
print(df1[['Student_ID', 'Total']])



import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

grade_cols = ['Math', 'English', 'Science']
df1['Average_Grade'] = df1[grade_cols].mean(axis=1).round(2)

top_student = df1.loc[df1['Average_Grade'].idxmax()]

df1['Total'] = df1[grade_cols].sum(axis=1)

subject_avg = df1[grade_cols].mean()

plt.bar(subject_avg.index, subject_avg.values, color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Average Grades by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Grade")
plt.ylim(0, 100)
plt.show()


import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()

print("Total sales for each product:")
print(total_sales)


import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)

max_sales_row = df2.loc[df2['Total_Sales'].idxmax()]

print("Date with highest total sales:")
print(max_sales_row[['Date', 'Total_Sales']])


import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

pct_change_df = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100

df2[['Product_A_pct', 'Product_B_pct', 'Product_C_pct']] = pct_change_df.round(2)

print("Percentage change in sales for each product from the previous day:")
print(df2[['Date', 'Product_A_pct', 'Product_B_pct', 'Product_C_pct']])


import pandas as pd
import matplotlib.pyplot as plt

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

plt.figure(figsize=(8,5))
plt.plot(df2['Date'], df2['Product_A'], marker='o', label='Product A')
plt.plot(df2['Date'], df2['Product_B'], marker='o', label='Product B')
plt.plot(df2['Date'], df2['Product_C'], marker='o', label='Product C')

plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()


import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

avg_salary = df3.groupby('Department')['Salary'].mean().reset_index()

print("Average salary for each department:")
print(avg_salary)

import pandas as pd

data = {
    'Employee': ['Ali', 'Laylo', 'Jasur', 'Madina', 'Sardor', 'Dilnoza'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'HR', 'Finance'],
    'Salary': [1200, 1000, 1500, 1300, 1100, 1600],
    'Experience': [3, 5, 7, 4, 6, 8]  
}

df = pd.DataFrame(data)


most_exp = df.loc[df['Experience'].idxmax()]

print("Employee with the most experience:")
print(most_exp[['Employee', 'Experience']])

import pandas as pd
data = {
    'Employee': ['Ali', 'Laylo', 'Jasur', 'Madina', 'Sardor', 'Dilnoza'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'HR', 'Finance'],
    'Salary': [1200, 1000, 1500, 1300, 1100, 1600],
    'Experience': [3, 5, 7, 4, 6, 8]
}

df = pd.DataFrame(data)


min_salary = df['Salary'].min()


df['Salary Increase'] = ((df['Salary'] - min_salary) / min_salary * 100).round(2)

print(df[['Employee', 'Salary', 'Salary Increase']])

import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Employee': ['Ali', 'Laylo', 'Jasur', 'Madina', 'Sardor', 'Dilnoza'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'HR', 'Finance'],
    'Salary': [1200, 1000, 1500, 1300, 1100, 1600],
    'Experience': [3, 5, 7, 4, 6, 8]
}

df = pd.DataFrame(data)


dept_counts = df['Department'].value_counts()

plt.figure(figsize=(6,4))
dept_counts.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Distribution of Employees Across Departments")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.show()


import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

total_revenue = df4['Total_Price'].sum()
print("Total Revenue:", total_revenue)


import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

product_orders = df4.groupby('Product')['Quantity'].sum()
most_ordered = product_orders.idxmax()
most_ordered_qty = product_orders.max()

print("Most Ordered Product:", most_ordered)
print("Total Quantity Ordered:", most_ordered_qty)

import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

avg_quantity = df4['Quantity'].mean()

print("Average Quantity of Products Ordered:", avg_quantity)


import pandas as pd
import matplotlib.pyplot as plt

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

sales_by_product = df4.groupby('Product')['Total_Price'].sum()

plt.figure(figsize=(6,6))
plt.pie(sales_by_product, labels=sales_by_product.index, autopct='%1.1f%%', startangle=90)
plt.title("Sales Distribution Across Products")
plt.show()





