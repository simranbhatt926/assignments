# 1) define 3 functions "add()","modify()" and "delete()" with just a print message.
# now accept input from user as a number. if the number entered is 1, call "add()"
# if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]

def add():
    print("Add function called.")

def modify():
    print("Modify function called.")

def delete():
    print("Delete function called.")

def main():
    user_input = int(input("Enter a number (1 for add, 2 for modify, 3 for delete): "))
    
    # Call function based on user input
    match user_input:
        case 1:
            add()
        case 2:
            modify()
        case 3:
            delete()
        case _:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


# 2) define a function which accepts a number and return its square.
  
def square_number(number):
    return number ** 2

num = float(input("Enter a number: "))
result = square_number(num)
print("The square of", num, "is", result)


#3) define a function which accepts character,int,string and display them.
   
    #  display_info, three parameters are accepted: char, integer, and string. These parameters correspond to a character,
    # an integer, and a string, respectively. The function then simply prints out each of these values with their corresponding labels.

def display_info(char, integer, string):
    print("Character:", char)
    print("Integer:", integer)
    print("String:", string)

char_input = input("Enter a character: ")[0]  # Take only the first character entered
integer_input = int(input("Enter an integer: "))
string_input = input("Enter a string: ")

display_info(char_input, integer_input, string_input)




#4) define "myfun1()" with a print statement. now define "myfun2()" which should invoke "myfun1()" function. 
def myfun1():
    print("This is myfun1.")

def myfun2():
    print("Invoking myfun1 from myfun2:")
    myfun1()

# Invoke myfun2
myfun2()



#5) define a function to accept a number. This function should return 1 if a number passed is more than 0
def check_number(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

num = float(input("Enter a number: "))
result = check_number(num)
print("Result:", result)




#6) define a function which accepts a character and return toggle of it. 

def toggle_character(char):
    # Check if the character is an alphabet
    if char.isalpha():
        # Toggle the case
        if char.islower():
            return char.upper()
        else:
            return char.lower()
    else:
        # Return non-alphabetic characters unchanged
        return char

# Example usage:
character = input("Enter a character: ")

# Ensure only the first character is considered
result = toggle_character(character[0])

print("Toggled character:", result)



#7) define a function which accepts a string , toggle and return it.
def toggle_string(input_string):
    return input_string.swapcase()

# Example usage:
input_str = input("Enter a string: ")
toggled_str = toggle_string(input_str)
print("Toggled string:", toggled_str)

#8) write a function to accept minimum 3 characters and maximum 5 characters. 
def process_string(input_string, min_length=3, max_length=5):
    if min_length <= len(input_string) <= max_length:
        print("Input string is within the specified length range.")
    else:
        print("Input string does not meet the length requirements.")

# Example usage:
user_input = input("Enter a string (minimum 3 characters, maximum 5 characters): ")
process_string(user_input)


#9) define a function in such a way that it can accept n number of values and print their sum.

def sum_values(*args):
    total = sum(args)
    print("Sum of the values:", total)

# Example usage:
sum_values(1, 2, 3, 4)
sum_values(5, 10, 15)
sum_values(2.5, 3.5, 4.5, 5.5, 6.5)

