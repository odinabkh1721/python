Task 1 


def is_prime(n):
       if n <= 1:
          return False  
       if n == 2:
          return True 
       for i in range(2, int(n ** 0.5) + 1):
          if n % i == 0:
              return False  
       return True  
print(is_prime(1))



# Task 1.2

def is_prime(n):
     if n <= 1:
         return False  
     if n == 2:
         return True  
     for i in range(2, int(n ** 0.5) + 1):
         if n % i == 0:
             return False  
     return True  

# print(is_prime(4))  


# Task 
def is_prime(n):
    if n <= 1:
         return False
    if n == 2:
      return True
      for i in range(2, int(n ** 0.5) + 1):
         if n % i == 0:
          return False
    return True  # bu return for tugaganidan keyin yozilishi kerak
print(is_prime(7))



# Task 2

def digit_sum(k):
  summa = 0
  for raqam in str(k):
    summa += int(raqam)
  return summa 
print(digit_sum(24)) 

# Task 2.2

def digit_sum(k):
     summa = 0
     for raqam in str(k):
         summa += int(raqam)
     return summa 
print(digit_sum(502))

# Task 3 

def powers_of_two(N):
   k = 0
   while 2 ** k <= N:
        print(2 **k)
   k +=1
print(powers_of_two(20))

# Task 3.2

def power_of_two(N):
    k = 0
    while 2 ** k <N:
        print(2 ** k)
        k +=1
print(power_of_two(10))
