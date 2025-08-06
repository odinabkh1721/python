
# HOMEWORK
# 1  Age Calculator: Ask the user to enter their birthdate. 
# Calculate and print their age in years, months, and days.

from datetime import date, datetime


birthday = input("when your birhtday(2007-3-16")


birthday = datetime.stprtime(birthday_input,"%2007-%3-%16")  # type: ignore

today = date.today()

age_days = (today - birthday).days

years = age_days //365
month = (age_days % 365) // 30
days = (age_days % 365) % 30 

print(f"Sizning yoshiningiz: {years} yil, {month} oy, {days} kun")


# 2 Days Until Next Birthday: Similar to the first exercise, but this time, calculate and 
print the number of days remaining until the user's next birthday.

from datetime import date, datetime

today = date.today()

birthday_input = input("Tug‘ilgan kuningizni yozing (2007-3-16): ")
birthday = datetime.strptime(birthday_input, "%2007-%3-%16").date()


this_year_birthday = date(today.year, birthday.month, birthday.day)

if this_year_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)
else:
    next_birthday = this_year_birthday


days_left = (next_birthday - today).days


print(f"Keyingi tug‘ilgan kungacha {days_left} kun qoldi.")

# 3.Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.


from datetime import datetime,timedelta 

today_time = input("joriy sana va vaqt kirit (2025-08-06 21:57:) " )


hours = int(input("Uchrashuv davomiyligi (soat): "))

minutes = int(input("Uchrashuv davomiyligi (daqiqa): "))

start_time = datetime.strptime(today_time, "%2025-%8-%6 %21:%57")
duration = timedelta(hours=hours, minutes=minutes)
end_time.strftime("%Y-%m-%d %H:%M")
print("Uchrashuv tugash vaqti:", end_time.strftime("%2025-%8-%6 %21:%57"))


# 4.Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert
#  and print the date and time in another timezone of their choice


from datetime import datetime
from zoneinfo import ZoneInfo


datetime_input = input("Sana va vaqtni kiriting (masalan: 2025-08-06 14:30): ")
current_timezone = input("Hozirgi vaqt zonangizni kiriting (masalan: Asia/Tashkent): ")
target_timezone = input("Qaysi vaqt zonaga o‘zgartirmoqchisiz? (masalan: Europe/London): ")

dt_object = datetime.strptime(datetime_input, "%Y-%m-%d %H:%M")


datetime_with_zone = dt_object.replace(tzinfo=ZoneInfo(current_timezone))

converted = datetime_with_zone.astimezone(ZoneInfo(target_timezone))


print("Natija:", converted.strftime("%Y-%m-%d %H:%M"), f"({target_timezone})")


# 5.Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time 
# remaining until that point in regular intervals (e.g., every second).


from datetime import datetime 
from time import sleep 

# 1. Foydalanuvchidan kelajak vaqtni olish
future_time = input("Kelajak vaqtni kiriting ( "%2025-%8-%7 %12:%32:%44")

# 2. Stringni datetime ga o‘tkazish
target_time = datetime.strptime(future_time, "%2025-%8-%7 %12:%32:%44")

while True:
    now = datetime.now()
    remaining = target_time - now

    if remaining.total_seconds() <= 0:
        print("⏰ Time's up!")
        break

    # Kun, soat, daqiqa, soniyani ajratib olish
    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"⏳ Qolgan vaqt: {days} kun {hours} soat {minutes} daqiqa {seconds} soniya", end="\r")
    sleep(1)


# 6.
# Email Validator: Write a program that validates email addresses. Ask the user to input an email address, 
# and check if it follows a valid email format.

import re

email = input("Email manzilni kiriting: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.fullmatch(pattern, email):
    print("✅ Email to‘g‘ri!")
else:
    print("❌ Noto‘g‘ri email manzili!")


# 7.Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. 
# For example, convert "1234567890" to "(123) 456-7890".

import re 
phone_number = input("Enter your phone number")
if re.fullmatch(r'\d{10}', phone_number):
    formatted = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
    print(" Formatlangan raqam:", formatted)
else:
    print("Noto‘g‘ri format. Iltimos, 10 ta raqam kiriting.")


# 8.
# Password Strength Checker: Implement a password strength checker. Ask the user to input a password and 
# check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

import re

password = input("Parol kiriting: ")

length_ok = len(password) >= 8
has_upper = re.search(r'[A-Z]', password)
has_lower = re.search(r'[a-z]', password)
has_digit = re.search(r'[0-9]', password)


if length_ok and has_upper and has_lower and has_digit:
    print("✅ Kuchli parol!")
else:
    print("❌ Parol kuchsiz. Quyidagilarni tekshiring:")
    if not length_ok:
        print("- Kamida 8 ta belgidan iborat bo‘lishi kerak")
    if not has_upper:
        print("- Kamida 1 ta KATTA harf bo‘lishi kerak")
    if not has_lower:
        print("- Kamida 1 ta kichik harf")


# 9.Word Finder: Develop a program that finds all occurrences of a specific word in a given text. 
# Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.


sample_text = """
Python is a powerful programming language. 
Many people use Python for data science, machine learning, web development, and more.
Python is also easy to learn.
"""

word = input("Qidirilayotgan so‘zni kiriting: ")

word_lower = word.lower()
text_lower = sample_text.lower()

count = text_lower.count(word_lower)

positions = []
start = 0
while True:
    index = text_lower.find(word_lower, start)
    if index == -1:
        break
    positions.append(index)
    start = index + 1

if count > 0:
    print(f"🔍 So‘z '{word}' matnda {count} marta uchradi.")
    print("📍 Joylashgan o‘rinlari (indexlar):", positions)
else:
    print(f"❌ So‘z '{word}' matnda topilmadi.")


# 10.Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, 
# and then identify and print all the dates present in the text.


import re

text = input("Matnni kiriting (ichida sanalar bo‘lsin): ")

date_pattern = r'\b(?:\d{1,2}[-/.]){2}\d{2,4}\b|\b\d{4}-\d{2}-\d{2}\b'


dates = re.findall(date_pattern, text)

if dates:
    print("Topilgan sanalar:")
    for d in dates:
        print("📅", d)
else:
    print("❌ Matnda sana topilmadi.")
