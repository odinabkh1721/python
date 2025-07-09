# Task 1

age = int(input("Enter your age: "))
name = (input ("Enter your name: "))
year = int(input("Enter your year: "))

print (age)

# Task 2

txt = 'LMaasleitbtui'
print(txt.split("Tesla","Subaru"))

# Task 3 3. Extract Car Names
txt = 'MsaatmiazD'
print(txt.split("Matiz"))

# Task 4 
txt = "I'am John. I am from London"
print(txt.split("I'am John. I am from"))

# Task 5 
word = "Python"
reverse = word[::-1]
print (reverse)

# Task 6 

word = "python"
print (word.count("aeiou"))

#  Task 7
numbers = input("5,7,8,15")
numbers_list = [int(number)]
max = max(numbers_list)
print ("Highest number : ",max)

# Task 8
soz = input("Good vibe: ").lower() 

if soz == soz[::-1]:
    print("Bu so'z palindrom")
else:
    print("Bu so'z palindrom emas.")

# Task 9 
email = input("bahodirovnaodina@gmail.com")
parts = email.split("@)")
print(parts)

# Task 10 

belgilar = string.ascii_letters + string.digits + string.punctuation

uzunlik = 10
parol = ''.join(random.choice(belgilar) for _ in range(uzunlik))

print("Tasodifiy parol:", parol)
