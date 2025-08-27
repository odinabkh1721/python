import pandas as pd 

df = pd.read_csv('tackoverflow_csv')   
print(df.head())

# 1 Find all questions that were created before 2014

import pandas as pd


df = pd.read_csv("tackoverflow_csv")


print(df.columns)


df['creationdate'] = pd.to_datetime(df['creationdate'])


questions_before_2014 = df[df['creationdate'] < "2014-01-01"]

print(questions_before_2014)
print("Umumiy soni:", len(questions_before_2014))


# 2 . Find all questions with a score more than 50

import pandas as pd 

df = pd.read_csv("tackoverflow_csv")   
print(df.columns)

score = df[df['score'] > 50]

print(score)


# 3 . Find all questions with a score between 50 and 100

import pandas as pd 

df = pd.read_csv("tackoverflow_csv")
print(df.columns)

score = df[df['score'].between(50,100)]

print(score)

# 4 Find all questions answered by Scott Boston 

import pandas as pd 

df = pd.read_csv("tackoverflow_csv")
print(df.columns)

scott_answers = df[df['ans_name'] == 'Scott Boston']

print(scott_answers)

# 5 Find all questions answered by the following 5 users 
import pandas as pd 

df = pd.read_csv("tackoverflow_csv")
print(df.columns)

users = ["Scott Boston", "User2", "User3", "User4", "User5"]


answers = df[df['ans_name'].isin(users)]

print(answers)


# 6 . Find all questions that were created between March,
# 2014 and October 2014 that were answered by Unutbu and have score less than 5.


import pandas as pd 


df = pd.read_csv("tackoverflow_csv")

print(df.columns)  

df['creationdate'] = pd.to_datetime(df['creationdate'])

result = df[
    (df['creationdate'] >= "2014-03-01") &
    (df['creationdate'] <= "2014-10-31") &
    (df['ans_name'] == "Unutbu") &
    (df['score'] < 5)
]

print(result)


# 7 Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

import pandas as pd 


df = pd.read_csv("tackoverflow_csv")

print(df.columns)  

result = df[
    (df["score"].between(5, 10)) |   
    (df["viewcount"] > 10000) 
]

# 8 Find all questions that are not answered by Scott Boston 

import pandas as pd 

df = pd.read_csv("tackoverflow_csv")
print(df.columns)

scott_not_answers = df[df['ans_name'] != 'Scott Boston']
print(scott_not_answers)


# Homework 3 Select Female Passengers in Class 1 with Ages between 
# 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30. 

import pandas as pd 

df = pd.read_csv("titanic_csv")
print(df.columns)


female_class1 = df[
    (df["Sex"] == "female") & 
    (df["Pclass"] == 1) & 
    (df["Age"].between(20, 30))
]

print(female_class1)


# 3 homework 2 Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

import pandas as pd 

df = pd.read_csv("titanic_csv")
print(df.columns)

Passangers = df[df['Fare'] >100]

print(Passangers)

# 3Homework Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).


import pandas as pd 

df = pd.read_csv("titanic_csv")
print(df.columns)

Passangers = df[df["Survived"]==0]
print(Passangers)


# 3 Homework 4 Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' 
# and paid more than $50.

import pandas as pd 

df = pd.read_csv("titanic_csv")
print(df.columns)

filtered = df[(df["Embarked"] == "C") & (df["Fare"] >50)]

print(filtered)


# 3 Homework 5 Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or
# spouses aboard and parents or children aboard.

import pandas as pd 

df = pd.read_csv("titanic_csv")
print(df.columns)

sibsp_parch = df[(df["SibSp"] > 0) & (df["Parch"] > 0)]
print("Siblings/Spouses va Parents/Children bo'lganlar:")
print(sibsp_parch)


# 3 Homework 6 Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.


import pandas as pd 

df = pd.read_csv("titanic_csv")
print(df.columns)

young_not_survived = df[(df["Age"] <= 15)  & (df["Survived"] == 00)]

print("15 yoshdan kichik va tirik qolmaganlar:")
print(young_not_survived)


# 3 Homeork 7 Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.

import pandas as pd 

df = pd.read_csv("titanic_csv")
print(df.columns)

cabin_fare = df[df["Cabin"].notna() & (df["Fare"] > 200)]
print("Kabinasi bor va $200 dan ko‘p to‘laganlar:")
print(cabin_fare)


# 3 Homework 8 Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

import pandas as pd 

df = pd.read_csv("titanic_csv")
print(df.columns)

odd_passenger_id = df[df["PassengerId"] % 2 == 1]
print("PassengerId toq bo'lganlar:")
print(odd_passenger_id)

















