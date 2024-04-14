#1	accept a number and display its table.
def display_table(n):
    print(f"Table of {n} : ")
    for i in range(1, 11):
        print(f"{n} *{ i} = {n*i}")
n=int(input("Enter the number: "))
display_table(n)            

#	2 using switch ….case   display whether accepted character is vowel or not.
character = input("Enter a character: ")
character = character.lower()
if character in ['a', 'e', 'i', 'o', 'u']:
    print(f"{character} is a vowel.")
else:
    print(f"{character} constant.")

# 3.Display numbers  1 to 10 using  While loop

number = 1
while number <=10:
    print(number)
    number +=1
#4.Display numbers from 3 to 30 except number 24  using while loop.

number = 3
while number <=30:
    if number != 24:
        print(number)
    number +=1
# 5.accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc. 
 
marks = float(input("Enter the marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 75:
    print("First Division")
elif marks >= 60:
    print("Second Division")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")

# 6.print the total of first 10 numbers.

print("for loop:")
for i in range(1, 11):
    print(i)

 #7. accept numbers till user enters 0 and display the total of all the numbers entered.
def calculate_total():
    total = 0
    while True:
        number = float(input("Enter a number (enter 0 to stop): "))
        if number == 0:
            break
        total += number
    return total


print("Total:", calculate_total())

# Calculate the total of numbers entered by the user
total = calculate_total()
print("Total of all numbers entered:", total)
     

#8. accept a character and display whether it is upper case or lower case or not an alphabet.

char = input("Enter a character: ")

# Check if the input is a single character
if len(char) != 1:
    print("Please enter only one character.")
else:
    # Check if the input is an alphabet
    if char.isalpha():
        # Check if the input is uppercase
        if char.isupper():
            print(char, "is an uppercase alphabet.")
        # Check if the input is lowercase
        elif char.islower():
            print(char, "is a lowercase alphabet.")
    else:
        print(char, "is not an alphabet.")
#9.display fibonicii series of 10 numbers

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(10):
    print(fibonacci(i))
#10. display prime numbers from 3 to 30
  
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Display prime numbers between 3 and 30
print("Prime numbers between 3 and 30:")
for num in range(3, 31):
    if is_prime(num):
        print(num)


#11.accept a number and display whether it is prime or not


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Take input from user
number = int(input("Enter a number: "))

# Check if the number is prime or not
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
