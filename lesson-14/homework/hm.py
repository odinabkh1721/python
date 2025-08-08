# Task: JSON Parsing
# write a Python script that reads the students.jon JSON file and prints details of each student.


import json 

with open ("students.json","r") as file:
    data = json.load(file)

    for student in data ["students"]:
        print(f"ID: {student ['id']}")
        print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grade: {student['grade']}")

    print("Subjects:")
    for subject in student["subjects"]:
        print(f" - {subject}")

        adress = student["addres"]
        print("Address:")
    print(f"  Street: {address['street']}") # type: ignore
    print(f"  City: {address['city']}") # type: ignore
    print(f"  State: {address['state']}") # type: ignore
    print(f"  Zipcode: {address['zipcode']}") # type: ignore
    
    print("-" * 40)


    # Task 2  import requests
import os

# API key — xavfsiz usul: environment variable
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
if not API_KEY:
    API_KEY = "YOUR_API_KEY"  # vaqtincha sinash uchun

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Shahar nomini kiriting: ").strip()

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params, timeout=10)

if response.status_code != 200:
    print("API bilan bog'lanishda xatolik:", response.status_code)
else:
    data = response.json()

    if data.get("cod") != 200:
        print("Xatolik:", data.get("message"))
    else:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌤 {city} ob-havosi:")
        print(f"Harorat: {temp}°C")
        print(f"Namlik: {humidity}%")
        print(f"Tavsif: {description}")
        print(f"Shamol tezligi: {wind_speed} m/s")



# 3 Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.



{
    "books": [
        {
            "id":1,
         "title":"The Great Gatsby",
        "author":"f.Scott Fitzgerald",
          "year": 1925
         },
         {
             "id":2,
             "title":"1965",
             "author":"George Ovell",
             "year":1943
        }
    ]

}


import json 
import os 

def load_books():
    if os.path.exists("books.json"):
        with open("books.json") as file:
             return json.load(file)
    return{"books":[]}

def save_books(data):
    with open("books.json", "w") as file:
        json.dump(data,file,indent=4)

def add_book():
    data = load_books()
    new_id = max([book["id"] for book in data [ "books"]], default = 0)+1
    title = input("enter new book: ")
    author = input("Enter author: ")
    year = input("Enter year")
    data["books"].append({"id": new_id,"title": title, "author":author,"year":year})
    save_books(data)
    print("Book added succesfully!")

def update_book():
    data = load_books()
    book_id = int(input("Enter book ID to update: "))
    for book in data["books"]:
        if book["id"] == book_id:
            book["title"] = input(f"Enter new title ({book['title']}): ") or book["title"]
            book["author"] = input(f"Enter new author ({book['author']}): ") or book["author"]
            year_input = input(f"Enter new year ({book['year']}): ")
            book["year"] = int(year_input) if year_input else book["year"]
            save_books(data)
            print("✏️ Book updated successfully!")
            return
    print(" Book not found!")

def delete_book():
    data = load_books()
    book_id = int(input("Enter book ID to delete: "))
    new_books = [book for book in data["books"] if book["id"] != book_id]
    if len(new_books) != len(data["books"]):
        data["books"] = new_books
        save_books(data)
        print("🗑 Book deleted successfully!")
    else:
        print(" Book not found!")

while True:
    print("\n📚 Book Manager")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()


# Task 4 

import requests
import random
import os

API_KEY = os.environ.get("OMDB_API_KEY")   
if not API_KEY:
    API_KEY = "YOUR_API_KEY"  

BASE_URL = "http://www.omdbapi.com/"

genre = input("Enter a movie genre (e.g., action, comedy, horror): ").strip()


params = {
    "s": genre,       
    "type": "movie",  
    "apikey": API_KEY
}

response = requests.get(BASE_URL, params=params, timeout=10)

if response.status_code != 200:
    print("API bilan bog'lanishda xatolik:", response.status_code)
else:
    data = response.json()
    if data.get("Response") == "False":
        print("Bu janr bo‘yicha hech narsa topilmadi.")
    else:
        movies = data.get("Search", [])
        chosen = random.choice(movies)

        imdb_id = chosen.get("imdbID")
        detail_params = {"i": imdb_id, "apikey": API_KEY}
        detail_resp = requests.get(BASE_URL, params=detail_params).json()

        print("\n🎬 Tavsiya qilingan film:")
        print(f"Title: {detail_resp.get('Title')}")
        print(f"Year: {detail_resp.get('Year')}")
        print(f"Genre: {detail_resp.get('Genre')}")
        print(f"Director: {detail_resp.get('Director')}")
        print(f"IMDB Rating: {detail_resp.get('imdbRating')}")
        print(f"Plot: {detail_resp.get('Plot')}")
