

import sqlite3 

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

conn.commit()
conn.close()

import sqlite3 

data ={
    '+Name':['David','Marli','Charlie'],
    'Species':['Human','Trill','Bajoran'],
    'Age':['40','300','29']
}

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

conn.commit()
conn.close()

import sqlite3 

data = [
    ("David", "Human", 40),
    ("Marli", "Trill", 300),
    ("Charlie", "Bajoran", 29)
]

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

conn.commit()
conn.close()


import sqlite3 

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("""
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Marli'
""")

conn.commit()
conn.close()


import sqlite3 

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT Name, Age
    FROM Roster
    WHERE Species = 'Bajoran'
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
